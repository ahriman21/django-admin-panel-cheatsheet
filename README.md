[ admin panel castomization ]
======================================================================
1-how to change admin HEADER & TITLE & INDEX TITLE:  
###### go to admin.py :  
###### admin.site.site_header = ' your header '  
###### admin.site.site_title = ' your title '   
###### admin.site.index_title = ' your index title'  
---
2-how to change appearance of  app names in admin panel :  
###### go to apps.py :  
###### verbose_name ='your optional name ' 
---
3-adding more information to tables in adminpanel :  
###### go to admin.py :  
###### list_display  = ('id' ,'title' , 'date' , 'category')  
---
4-adding a external field to table :   
###### def get_author(self,current_record):
###### ....return  current_record.user.username
###### get_author.short_description = 'author'
###### list_display( 'get_author',)
---

5-how to do editable boolean fields as CHECK in table : ✔ ❌  
###### list_editable = ('is_admin',)  
###### you can add numeric fields as well or little textboxes .  

---

6-enable search in admin panel: 🔍  
###### search_fileds = ('coulomns you want to search in', 'x','y')  

---

7-enable filters in admin panel: 🔎  
###### list_filter = ('x','y')  

---

8-sort and order table records in admin pnale :  
###### sortable_by = ('id','age','title','is_admin')  
###### ordering = ('id','age')  

---

9-how to customize the editing page of a detail object in admin pnel :  
###### change sequense of form fields :  
###### fields  = ('title','text','category')  
###### readonly_fields = ('created_time')  

---

10-initialize new action in django admin panel :  
###### define a function with thease argumans => (self,request,queryset)  
###### write your code for the action you want using "queryset" but don't return anything.  
###### show message to user after action happened using "self.message_user(request, 'your message')"  
###### actions = ('name of the function',)  

---

11- how to display a empty-value-filed in table :
###### empty_value_display = 'UNSET' 

--- 

12- to change the position of save button:
###### save_on_top = True
