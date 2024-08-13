def execute_orm():
    pass
    #  Total number of Books

    # books_count = Book.objects.count()
    # print(books_count)

    # Avg,sum,min,max of all Books

    # avg = Book.objects.aggregate(price = Avg('price'))
    # sum = Book.objects.aggregate(total_price = Sum('price') )
    # min = Book.objects.aggregate(min_price = Min('price'))
    # max = Book.objects.aggregate(min_price = Max('price'))
    # print(avg,sum,min,max)

    # Total books written by each author
    # authors = Author.objects.annotate(total_books = Count('book'))
    # for author in authors:
    #     print(f"{author.author_name} ==> Total Books {author.total_books}")

    # Annotate each author with the average price of their books

    # authors_with_avg_price = Author.objects.annotate(avg_price=Avg('book__price'))

    # for author in authors_with_avg_price:
    #     print(f"Author: {author.author_name}, Average Book Price: {author.avg_price}")
    
    
    

    # authors_with_many_books = Author.objects.annotate(total_books=Count("book")).filter(
    #     total_books__gt=3
    # )
    # for author in authors_with_many_books:
    #     print(f"Author: {author.author_name}, Total Books: {author.total_books}")
    
    
    
    
    # Annotate each author with the total number of books published in 2023
    # authors_with_books_2023 = Author.objects.annotate(
    #     books_2023=Count('book', filter=Q(book__publish_date__year=2023))
    # )

    # for author in authors_with_books_2023:
    #     print(f"Author: {author.author_name}, Books Published in 2023: {author.books_2023}")
    
    
    # Annotate each author with both the total number of books and the average price of their books
    # authors_with_stats = Author.objects.annotate(
    #     total_books=Count('book'), avg_price=Avg('book__price'))

    # for author in authors_with_stats:
    #     print(f"Author: {author.author_name}, Total Books: {author.total_books}, Average Book Price: {author.avg_price}")
    
    
    # 7. Most expensive books for each author
    # authors = Author.objects.annotate(expensive_book = Max('book__price'))
    
    # for author in authors:
    #     print(f'{author.author_name}----> maxprice of books {author.expensive_book}')
    
    # Authors with atleast One book priced over 50$
    # authors = Author.objects.annotate(book_count = Count('book', filter=Q(book__price__gte=50))).filter(book_count__gte=1)
    
    # for author in authors:
    #     print(f'{author.author_name}----> no of books more than $50 ==> {author.book_count}')
    
    # 9. Total earning for each Authors
    # authors = Author.objects.annotate(total_price = Sum('book__price'))
    
    # for author in authors:
    #     print(f"{author.author_name} total book price: {author.total_price}")
    
    # 10. Combining multiple Aggregations
    
    # authors = Author.objects.annotate(total_books_in_2023 = Count('book',filter=Q(book__publish_date__year = 2023)),
    #                                   total_earning = Sum('book__price'))
    
    # for author in authors:
    #     print(f"{author.author_name}==>earning=>{author.total_earning} total_books->{author.total_books_in_2023}")


execute_orm()