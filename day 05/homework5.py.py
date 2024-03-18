#starting price rename veriables
book1_price = 10
book2_price = 20
book3_price = 30
book4_price = 40
book5_price = 50
book6_price = 60
book7_price = 70
book8_price = 80
book9_price = 90
book10_price = 100
#declaring velues of discounts


small_discount = 10
large_discount = 20

#declaring value of book after discount
#declaring small discounts
book1_afther_small_discount = book1_price - (book1_price * small_discount/100)
book_small_discount2 = book2_price * small_discount/100
book_small_discount3 = book3_price * small_discount/100
book_small_discount4 = book4_price * small_discount/100
book_small_discount5 = book5_price * small_discount/100
#declaring of values large discounts
book_large_discount1 = book1_price * small_discount/100
book_large_discount2 = book2_price * small_discount/100
book_large_discount3 = book3_price * small_discount/100
book_large_discount4 = book4_price * small_discount/100
book_large_discount5 = book5_price * small_discount/100
#displayng last prices of books with small discount
print("book1'sprise is",book1_afther_small_discount,"book2's prise is",book_small_discount2,
      "book3's prise is",book_small_discount3,"book4's price is",book_small_discount4
      ,"book5's price is",book_small_discount5)

#displaying last prices of book whith large discount
print("book6 costs",book_large_discount1,"book7 costs",book_large_discount2,
      "book8 costs",book_large_discount3,"book9 costs",book_large_discount4,
      "book10 costs",book_large_discount5,)


