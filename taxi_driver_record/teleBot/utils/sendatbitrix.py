async def send_to_bitrix(doc_name):
    #from fast_bitrix24 import Bitrix
    from fast_bitrix24 import BitrixAsync
    import base64
    #webhook = "https://b24-51i8uh.bitrix24.ru/rest/1/ov8wzelmx6s1ouw7/"  # my

    webhook = "https://vitabo.bitrix24.ru/rest/14/ie9rvv2gfhfjlctk/" #bodya
    b = BitrixAsync(webhook)
    from PIL import Image
    from io import BytesIO
    #бот видит только у андрея тимофеева
    with open(f"WordFiles/{doc_name}.docx", "rb") as binary_file:
        binary_file_data = binary_file.read()
        binary64_encode_data = base64.b64encode(binary_file_data)
        base64_message = binary64_encode_data.decode('utf-8')

    res_file_disk_upload =await b.call("disk.folder.uploadfile", {
        'id': 65096,
        'data': {
            'NAME': f"{doc_name}.docx"
        },
        'fileContent': base64_message
    })


    # await b.call('crm.deal.add', {'fields': {'TITLE': doc_name,
    #                                    'COMMENTS': res_file_disk_upload['DOWNLOAD_URL'],
    #                                    'STATUS_ID ':'C4:UC_CA60XF',
    #                                          "CATEGORY_ID": "4"}})


    await b.call('crm.deal.add', {'fields': {'TITLE': doc_name,
                                       'COMMENTS': res_file_disk_upload['DOWNLOAD_URL'],
                                       'STATUS_ID ':'C26:NEW',
                                             "CATEGORY_ID": "26"}})

#

#'STATUS_ID ':'C26:NEW', "CATEGORY_ID": "26"}})
    #
    # await b.call('crm.lead.add', {'fields': {'TITLE': doc_name,
    #                                   'UF_CRM_1650626903':res_file_disk_upload['DOWNLOAD_URL'],
    #
    #                                   }})