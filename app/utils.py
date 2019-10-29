import json
import os
from pprint import pprint
import re

from win32com import client


def find_builds(build, tag):
    with open(r'c:\experiments\work_py\cfg.json') as fi:
        cfg_dct = json.load(fi)

    patt = re.compile(r'-%s(_x64)*__(git--)*%s$' % (build, tag), re.I)
    search_dirs = [os.path.join(cfg_dct['root_dir'], item) for item in cfg_dct['prod_dirs']]
    setups = list()

    for _dir in search_dirs:
        obj = os.scandir(_dir)
        for item in obj:
            if re.search(patt, item.name):
                setups.append(item.path)
    return setups


# result = list()
# with open('snap_dct.json') as fi:
#     vms = json.load(fi)
#
# for _setup in setups:
#     setup_prefix = os.path.basename(_setup).split('-')[0]
#     snapshot_prefix = cfg_dct['prod_snaps'][setup_prefix]
#     for _vm in vms:
#         vm_name = _vm.replace('.vmx', '')
#         vm_path = vms[_vm]['pth']
#         for k in vms[_vm]['sn']:
#             if k.startswith(snapshot_prefix):
#                 result.append((_setup,  vm_name, vm_path,  k, "0"))
#
# # pprint(result)
#
# job_file = r'c:\experiments\work_py\VM-Monitor.Jobs.xls'
# xls = client.Dispatch("Excel.Application")
# wb = xls.Workbooks.Add()
# sheet = wb.WorkSheets("Sheet1")
# sheet.Name = "Table"

# header
# header_list = ["InstallPath", "Name", "Path", "SnapName", "Done"]
# for i in range(len(header_list)):
#     sheet.Cells(1, i + 1).value = header_list[i]
#
# for i in range(len(result)):
#     for j in range(5):
#         # print(result[i][j])
#         sheet.Cells(i + 2, j + 1).value = result[i][j]
#
# wb.SaveAs(job_file, 56)
# wb.Close()

