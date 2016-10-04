from .pydc import DCRecord

def build_dc_record(dc_dict):
	dc_record = DCRecord()
	for key in dc_dict.keys():
		dc_record.add_field(key, dc_dict[key])
	return dc_record