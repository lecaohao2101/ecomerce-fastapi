# from sqladmin import BaseView, expose
#
# class RequestAdmin(BaseView):
#     name = "Request"
#     icon = "fa-chart-line"
#
#     @expose("/report", methods=["GET"])
#     def report_page(self, request):
#         return self.templates.TemplateResponse(
#             "report.html",
#             context={"request": request},
#         )