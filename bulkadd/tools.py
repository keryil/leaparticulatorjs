from django.contrib.admin.actions import delete_selected
import object_tools


class BulkAdd(object_tools.ObjectTool):
    name = 'bulkadd'
    label = 'Bulk add'

    def view(self, request, extra_context=None):
        queryset = self.model.objects.all()
        response = delete_selected(self.modeladmin, request, queryset)
        if response:
            return response
        else:
            return self.modeladmin.changelist_view(request)

object_tools.tools.register(BulkAdd)
