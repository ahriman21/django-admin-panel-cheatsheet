# if you wanna write your own filtering in sidebar of adminpanel you can create a subclass that has a superclass named 'admin.SimpleListFilter' and 
# define two functions , one for label and one for querysets by each label .

# -1 : write your filter
class FilterByDifficulty(admin.SimpleListFilter):
  title = 'difficulty'                   # --> the title that displays in adminpanel sidebar.
  parameter_name = 'time_estimate_hours' # --> the model field you want to filter  by .
  
  def lookups(self,request,model_admin):
    return (
      ('hard','Hard'),
      ('mid','Mid'),
      ('easy','Easy),
    )
  
      
  def queryset(self,request,queryset):
      if self.value = 'hard':
        return queryset.filter(time_estimate_hours__gt = 5) # --> the ones that are >= 5.
      elif self.value = 'mid':
        return queryset.filter(time_estimate_hours__gte = 3 ,time_estimate_hours__lte = 5 ) # the ones that are between 3 and 5
      elif self.value = 'easy':
        return queryset.filter(time_estimate_hours__lt = 3 ) # the ones that are less than 3
      
      
      
 # - 2 : define in ModelAdmin class:
 class ToDoItemAdmin(admin.ModelAdmin):
      list_filter(FilterByDifficulty)
      
  
