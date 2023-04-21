from sqladmin import BaseView, expose

from src.database.models import CategoryRequest
from src.helpers.permission import check_role_access, check_role_view


class RequestAdmin(BaseView):
    name = "Request"
    icon = "fa-chart-line"

    @expose("/", methods=["GET"])
    def report_page(self, request):
        return self.templates.TemplateResponse(
            "index.html",
            context={"request": request},
        )
