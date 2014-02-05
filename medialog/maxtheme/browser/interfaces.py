from plone.theme.interfaces import IDefaultPloneLayer
from plone.app.portlets.interfaces import IColumn

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "Maxtheme Theme" theme, this interface must be its layer
       (in maxtheme/viewlets/configure.zcml).
    """
    
class IMaxthemeTopContent(IColumn):
    """we need our own portlet manager in the top area.
    """