# django-admin-panel
django admin panel tools 
<!--  -->
admin panel castomization :
========================================================================
* how to change admin HEADER & TITLE & INDEX TITLE:
-go to admin.py :
-- admin.site.site_header = ' your header '

-- admin.site.site_title = ' your title ' 

-- admin.site.index_title = ' your index title'
========================================================================
* how to change appreance of  app names in admin panel :
-go to apps.py :
-- verbose_name = ' your optional name '
========================================================================
*adding more information to tables in adminpanel :
-go to admin.py :
-- list_table  = ('id' ,'title' , 'date' , 'category')
========================================================================
**adding a external field to table :  
-- def get_author(self,current_record):
	return  current_record.user.username
-- list_table( 'get_author',)
========================================================================
* how to do editable boolean fields as CHECK in table : ✔ ❌
-- list_editable = ('is_admin',)
you can add numeric fields as well or little textboxes .
========================================================================
* enable search in admin panel: 🔍
-- search_fileds = ('coulomns you want to search in', 'x','y')
========================================================================
* enable filters in admin panel: 🔎
-- list_filter = ('x','y')
========================================================================
* sort and order table records in admin pnale :
-- sortable_by = ('id','age','title','is_admin')
-- ordering = ('id','age')
========================================================================
*how to customize the editing page of a detail object in admin pnel :
** change sequense of form fields :
-- fields  = ('title','text','category')
-- readonly_fields = ('created_time')

========================================================================
* initialize new action in django admin panel :
-- define a function with thease argumans => (self,request,queryset)
-- write your code for the action you want using "queryset" but don't return anything.
-- show message to user after action happened using "self.message_user(request, 'your message')"
-- > actions = ('name of the function',)

=========================================================================
*add image to admin panel's table
*field sets 
*show more information to users based on roles


