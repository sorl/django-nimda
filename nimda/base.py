class NimdaException(Exception):
    pass


class NimdaSiteMixin(object):
    def each_context(self, request):
        """
        Adds available_apps to each context
        """
        c = super(NimdaSiteMixin, self).each_context(request)
        res = self.index(request)
        c['available_apps'] = res.context_data['app_list']
        return c
