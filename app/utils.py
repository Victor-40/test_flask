import json
import os
from pprint import pprint
import re
from win32com import client
import pythoncom


def find_builds(build, tag, _prod):
    with open(r'c:\experiments\work_py\cfg.json') as fi:
        cfg_dct = json.load(fi)

    patt = re.compile(r'-%s(_x64)*__(git--)*%s$' % (build, tag), re.I)

    full_prod = cfg_dct['prod_dirs']
    work_prod = list()
    for i in _prod:
        for j in full_prod:
            if j.startswith(i):
                work_prod.append(j)
    search_dirs = [os.path.join(cfg_dct['root_dir'], item) for item in work_prod]
    setups = list()

    for _dir in search_dirs:
        obj = os.scandir(_dir)
        for item in obj:
            if re.search(patt, item.name):
                setups.append(item.path)
    return setups


def make_xls(setups):
    result = list()
    with open(r'c:\experiments\test_flask\app\cfg.json') as fi:
        cfg_dct = json.load(fi)

    with open(r'c:\experiments\test_flask\app\snap_dct.json') as fi:
        vms = json.load(fi)

    for _setup in setups:
        setup_prefix = os.path.basename(_setup).split('-')[0]
        snapshot_prefix = cfg_dct['prod_snaps'][setup_prefix]
        for _vm in vms:
            vm_name = _vm.replace('.vmx', '')
            vm_path = vms[_vm]['pth']
            for k in vms[_vm]['sn']:
                if k.startswith(snapshot_prefix):
                    result.append((_setup,  vm_name, vm_path,  k, "0"))

    job_file = r'c:\experiments\test_flask\VM-Monitor.Jobs.xls'
    pythoncom.CoInitialize()
    xls = client.Dispatch("Excel.Application")

    wb = xls.Workbooks.Add()
    sheet = wb.WorkSheets("Sheet1")
    sheet.Name = "Table"

    # header
    header_list = ["InstallPath", "Name", "Path", "SnapName", "Done"]
    for i in range(len(header_list)):
        sheet.Cells(1, i + 1).value = header_list[i]

    for i in range(len(result)):
        for j in range(5):
            sheet.Cells(i + 2, j + 1).value = result[i][j]

    wb.SaveAs(job_file, 56)
    wb.Close()
    pythoncom.CoUninitialize()

    return result


def make_dir_list(_prefix, _subdir):
    # print(_prefix, _subdir)
    root = r'\\svr-rum-net-04\new_versions'
    path = os.path.join(root, _prefix, _subdir)
    print(path)
    setups_d = list()

    obj = os.scandir(path)

    if _subdir == '_External':
        for item in obj:
            sp = os.path.join(item.name, os.listdir(item.path)[0])
            setups_d.append((os.path.join(path, sp), sp))
        return sorted(setups_d)

    for item in obj:
        if item.name.startswith(_prefix):
            setups_d.append((item.path, item.name))
    return sorted(setups_d)

