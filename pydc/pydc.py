from lxml import etree as ET

__version__ = '0.1'

# declare namespaces
DC_NS = "http://purl.org/dc/elements/1.1/"
DCTERMS_NS = "http://purl.org/dc/terms/"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"


dc_nsmap = {
    "dc": DC_NS,
    "dcterms": DCTERMS_NS,
    "xsi": XSI_NS,
}

ET.register_namespace('dc', DC_NS)
ET.register_namespace('dcterms', DCTERMS_NS)
ET.register_namespace('xsi', XSI_NS)

class DCRecord(ET.ElementBase):
    """For building a Dublin Core record. Handles the following namespaces:
    http://purl.org/dc/elements/1.1/ (as the "dc" prefix)
    http://purl.org/dc/terms/ (as the "dcterms" prefix)
    http://www.w3.org/2001/XMLSchema-instance (as the "xsi" prefix, for 
    attributes)
    """
    TAG = "{%s}record" % (DC_NS,)


    def __init__(self):
        super(DCRecord, self).__init__(nsmap=dc_nsmap)

    def add_field(self, key, value):
        tag = key
        if " " in tag:
            tag_list = tag.split(" ")
            tag = tag_list[0]
            attribute = tag_list[1]
        else:
            attribute = None
        tag_components = tag.split(":")
        tag_prefix = tag_components[0]
        tag_name = tag_components[1]
        if attribute:
            # split up the attribute from its value
            attribute_details = attribute.split("=")
            attribute = attribute_details[0]
            attribute_value = attribute_details[1]
            if ":" in attribute:
                attribute_components = attribute.split(":")
                attribute_prefix = attribute_components[0]
                attribute_name = attribute_components[1]
            else:
                attribute_name = attribute
                attribute_prefix = None
        # first, most complex circumstance:
        # does it have a namespaced attribute?
        if attribute and attribute_prefix:
            if tag_prefix == "dc":
                element = ET.Element("{%s}%s" % (DC_NS, tag_name))
            elif tag_prefix == "dcterms":
                element = ET.Element("{%s}%s" % (DCTERMS_NS, tag_name))
            if attribute_prefix == "xsi":
                element.set("{%s}%s" % (XSI_NS, attribute_name), attribute_value)
            element.text = value
            self.append(element)
        # if not, does it have an un-namespaced attribute?
        elif attribute and attribute_name:
            if tag_prefix == "dc":
                element = ET.Element("{%s}%s" % (DC_NS, tag_name))
            elif tag_prefix == "dcterms":
                element = ET.Element("{%s}%s" % (DCTERMS_NS, tag_name))
            element.set("%s" % (attribute_name))
            element.text = value
            self.append(element)
        else:
            if tag_prefix == "dc":
                element = ET.Element("{%s}%s" % (DC_NS, tag_name))
            elif tag_prefix == "dcterms":
                element = ET.Element("{%s}%s" % (DCTERMS_NS, tag_name))
            element.text = value
            self.append(element)