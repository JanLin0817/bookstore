from django.contrib import admin
from .models import Book

# 方法 1：簡單註冊（一行搞定）
admin.site.register(Book)

# from django.contrib import admin
# from .models import Book

# # 方法 2：進階註冊（可以自訂很多功能）
# @admin.register(Book)  # 裝飾器語法
# class BookAdmin(admin.ModelAdmin):
#     # 在列表頁顯示哪些欄位
#     list_display = ['title', 'author', 'year', 'rating', 'created_at']
    
#     # 可以搜尋哪些欄位
#     search_fields = ['title', 'author']
    
#     # 右側可以用哪些欄位篩選
#     list_filter = ['year', 'rating']
    
#     # 每頁顯示幾筆資料
#     list_per_page = 20