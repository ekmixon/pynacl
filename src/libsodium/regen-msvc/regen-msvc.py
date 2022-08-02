#! /usr/bin/env python3

import glob
import os
import uuid

dirs = set()

tlv1 = ""
for file in glob.iglob("src/libsodium/**/*.c", recursive=True):
    file = file.replace("/", "\\")
    tlv1 = tlv1 + f'    <ClCompile Include="{file}" />\r\n'

tlv2 = ""
for file in glob.iglob("src/libsodium/**/*.h", recursive=True):
    file = file.replace("/", "\\")
    tlv2 = tlv2 + f'    <ClInclude Include="{file}" />\r\n'

tlf1 = ""
for file in glob.iglob("src/libsodium/**/*.c", recursive=True):
    file = file.replace("/", "\\")
    tlf1 = tlf1 + f'    <ClCompile Include="{file}">\r\n'
    tlf1 = tlf1 + "      <Filter>Source Files</Filter>\r\n"
    tlf1 = tlf1 + "    </ClCompile>\r\n"

tlf2 = ""
for file in glob.iglob("src/libsodium/**/*.h", recursive=True):
    file = file.replace("/", "\\")
    tlf2 = tlf2 + f'    <ClInclude Include="{file}">\r\n'
    tlf2 = tlf2 + "      <Filter>Header Files</Filter>\r\n"
    tlf2 = tlf2 + "    </ClInclude>\r\n"

v1 = ""
for file in glob.iglob("src/libsodium/**/*.c", recursive=True):
    file = file.replace("/", "\\")
    v1 = v1 + f'    <ClCompile Include="..\\..\\..\\..\\{file}" />\r\n'

v2 = ""
for file in glob.iglob("src/libsodium/**/*.h", recursive=True):
    file = file.replace("/", "\\")
    v2 = v2 + f'    <ClInclude Include="..\\..\\..\\..\\{file}" />\r\n'

f1 = ""
for file in glob.iglob("src/libsodium/**/*.c", recursive=True):
    basedir = os.path.dirname(file).replace("src/libsodium/", "")
    t = basedir
    while t != "":
        dirs.add(t)
        t = os.path.dirname(t)
    basedir = basedir.replace("/", "\\")
    file = file.replace("/", "\\")
    f1 = f1 + f'    <ClCompile Include="..\\..\\..\\..\\{file}">\r\n'
    f1 = f1 + f"      <Filter>{basedir}</Filter>\r\n"
    f1 = f1 + "    </ClCompile>\r\n"

f2 = ""
for file in glob.iglob("src/libsodium/**/*.h", recursive=True):
    basedir = os.path.dirname(file).replace("src/libsodium/", "")
    t = basedir
    while t != "":
        dirs.add(t)
        t = os.path.dirname(t)
    basedir = basedir.replace("/", "\\")
    file = file.replace("/", "\\")
    f2 = f2 + f'    <ClInclude Include="..\\..\\..\\..\\{file}">\r\n'
    f2 = f2 + f"      <Filter>{basedir}</Filter>\r\n"
    f2 = f2 + "    </ClInclude>\r\n"

fd = ""
dirs = sorted(dirs)
for dir in dirs:
    dir = dir.replace("/", "\\")
    uid = uuid.uuid3(uuid.UUID(bytes=b"LibSodiumMSVCUID"), dir)
    fd = fd + f'    <Filter Include="{dir}">\r\n'
    fd = fd + "      <UniqueIdentifier>{{{}}}</UniqueIdentifier>\r\n".format(
        uid
    )
    fd = fd + "    </Filter>\r\n"


def apply_template(tplfile, outfile, sbox):
    tpl = ""
    with open(tplfile, "rb") as fd:
        tpl = fd.read()
    for s in sbox.keys():
        tpl = tpl.replace(
            str.encode("{{" + s + "}}", "utf8"),
            str.encode(str.strip(sbox[s]), "utf8"),
        )

    with open(outfile, "wb") as fd:
        fd.write(tpl)


sbox = {
    "tlv1": tlv1,
    "tlv2": tlv2,
    "tlf1": tlf1,
    "tlf2": tlf2,
    "v1": v1,
    "v2": v2,
    "f1": f1,
    "f2": f2,
    "fd": fd,
}

sd = os.path.dirname(os.path.realpath(__file__))

apply_template(
    f"{sd}/tl_libsodium.vcxproj.filters.tpl", "libsodium.vcxproj.filters", sbox
)


sbox["platform"] = "v140"
apply_template(f"{sd}/tl_libsodium.vcxproj.tpl", "libsodium.vcxproj", sbox)

apply_template(
    f"{sd}/libsodium.vcxproj.filters.tpl",
    "builds/msvc/vs2019/libsodium/libsodium.vcxproj.filters",
    sbox,
)

apply_template(
    f"{sd}/libsodium.vcxproj.filters.tpl",
    "builds/msvc/vs2017/libsodium/libsodium.vcxproj.filters",
    sbox,
)

apply_template(
    f"{sd}/libsodium.vcxproj.filters.tpl",
    "builds/msvc/vs2015/libsodium/libsodium.vcxproj.filters",
    sbox,
)

apply_template(
    f"{sd}/libsodium.vcxproj.filters.tpl",
    "builds/msvc/vs2013/libsodium/libsodium.vcxproj.filters",
    sbox,
)

apply_template(
    f"{sd}/libsodium.vcxproj.filters.tpl",
    "builds/msvc/vs2012/libsodium/libsodium.vcxproj.filters",
    sbox,
)

apply_template(
    f"{sd}/libsodium.vcxproj.filters.tpl",
    "builds/msvc/vs2010/libsodium/libsodium.vcxproj.filters",
    sbox,
)


sbox["platform"] = "v142"
apply_template(
    f"{sd}/libsodium.vcxproj.tpl",
    "builds/msvc/vs2019/libsodium/libsodium.vcxproj",
    sbox,
)


sbox["platform"] = "v141"
apply_template(
    f"{sd}/libsodium.vcxproj.tpl",
    "builds/msvc/vs2017/libsodium/libsodium.vcxproj",
    sbox,
)


sbox["platform"] = "v140"
apply_template(
    f"{sd}/libsodium.vcxproj.tpl",
    "builds/msvc/vs2015/libsodium/libsodium.vcxproj",
    sbox,
)


sbox["platform"] = "v120"
apply_template(
    f"{sd}/libsodium.vcxproj.tpl",
    "builds/msvc/vs2013/libsodium/libsodium.vcxproj",
    sbox,
)


sbox["platform"] = "v110"
apply_template(
    f"{sd}/libsodium.vcxproj.tpl",
    "builds/msvc/vs2012/libsodium/libsodium.vcxproj",
    sbox,
)


sbox["platform"] = "v100"
apply_template(
    f"{sd}/libsodium.vcxproj.tpl",
    "builds/msvc/vs2010/libsodium/libsodium.vcxproj",
    sbox,
)
