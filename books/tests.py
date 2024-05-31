from django.test import TestCase
from django.urls import reverse
from .models import Author, Book


class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Author 1", bio="Author bio")

    def test_author_str(self):
        self.assertEqual(str(self.author), self.author.name)


class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Author 1", bio="Author bio")
        self.book = Book.objects.create(
            title="Book 1",
            description="Book description",
            publication_date="2023-01-01",
            price=19.99
        )
        self.book.authors.add(self.author)

    def test_book_str(self):
        self.assertEqual(str(self.book), self.book.title)


class BookListViewTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Author 1", bio="Author bio")
        self.book1 = Book.objects.create(
            title="Book 1",
            description="Book 1 description",
            publication_date="2023-01-01",
            price=19.99
        )
        self.book1.authors.add(self.author)
        self.book2 = Book.objects.create(
            title="Book 2",
            description="Book 2 description",
            publication_date="2023-01-02",
            price=29.99
        )
        self.book2.authors.add(self.author)

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')
        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book2.title)


class BookDetailViewTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Author 1", bio="Author bio")
        self.book = Book.objects.create(
            title="Book 1",
            description="Book description",
            publication_date="2023-01-01",
            price=19.99
        )
        self.book.authors.add(self.author)

    def test_book_detail_view(self):
        response = self.client.get(reverse('book_detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_detail.html')
        self.assertContains(response, self.book.title)
        self.assertContains(response, self.book.description)


class AuthorListViewTest(TestCase):
    def setUp(self):
        self.author1 = Author.objects.create(name="Author 1", bio="Author 1 bio")
        self.author2 = Author.objects.create(name="Author 2", bio="Author 2 bio")

    def test_author_list_view(self):
        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author_list.html')
        self.assertContains(response, self.author1.name)
        self.assertContains(response, self.author2.name)


class AuthorDetailViewTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Author 1", bio="Author bio")

    def test_author_detail_view(self):
        response = self.client.get(reverse('author_detail', args=[self.author.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author_detail.html')
        self.assertContains(response, self.author.name)
        self.assertContains(response, self.author.bio)


class OrderedBooksViewTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Author 1", bio="Author bio")
        self.book1 = Book.objects.create(
            title="A Book",
            description="Book 1 description",
            publication_date="2023-01-01",
            price=19.99
        )
        self.book1.authors.add(self.author)
        self.book2 = Book.objects.create(
            title="B Book",
            description="Book 2 description",
            publication_date="2023-01-02",
            price=29.99
        )
        self.book2.authors.add(self.author)

    def test_ordered_books_view(self):
        response = self.client.get(reverse('ordered_books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list_ordered.html')
        books = list(response.context['books'])
        self.assertEqual(books, [self.book1, self.book2])  # Ensure books are ordered by title
