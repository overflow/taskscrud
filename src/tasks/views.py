from django.conf.urls import url, include

from cruds_adminlte import utils
from cruds_adminlte.crud import CRUDView

from tasks.models import Task


class TaskView(CRUDView):
    check_login = True
    check_perms = False
    model = Task

    def get_urls(self):

        pre = ""
        try:
            if self.cruds_url:
                pre = "%s/" % self.cruds_url
        except AttributeError:
            pre = ""
        myurls = []
        if 'list' in self.views_available:
            myurls.append(url("list$",
                              self.list,
                              name=utils.crud_url_name(
                                  self.model, 'list', prefix=self.urlprefix)))
            myurls.append(url("^$",
                              self.list,
                              name=utils.crud_url_name(
                                  self.model, 'list', prefix=self.urlprefix)))
        if 'create' in self.views_available:
            myurls.append(url("^create$",
                              self.create,
                              name=utils.crud_url_name(
                                  self.model, 'create', prefix=self.urlprefix))
                          )
        if 'detail' in self.views_available:
            myurls.append(url('^(?P<pk>[^/]+)$',
                              self.detail,
                              name=utils.crud_url_name(
                                  self.model, 'detail', prefix=self.urlprefix))
                          )
        if 'update' in self.views_available:
            myurls.append(url("^(?P<pk>[^/]+)/update$",
                              self.update,
                              name=utils.crud_url_name(
                                  self.model, 'update', prefix=self.urlprefix))
                          )
        if 'delete' in self.views_available:
            myurls.append(url(r"^(?P<pk>[^/]+)/delete$",
                              self.delete,
                              name=utils.crud_url_name(
                                  self.model, 'delete', prefix=self.urlprefix))
                          )

        myurls += self.add_inlines('')
        return myurls
