import os

def find_src_openeuler_dirs(start_dir):
    src_openeuler_dirs = []
    for root, dirs, files in os.walk(start_dir):
        for dir_name in dirs:
            if dir_name == "src-openeuler":
                src_openeuler_dirs.append(os.path.join(root, dir_name))
    return src_openeuler_dirs

def find_sig_dirs(result):
    sig_name = []
    for path in result:
        dir_path, _ = os.path.split(path)
        dir_path = dir_path.lstrip('./')
        sig_name.append(dir_path)
    return sig_name

if __name__ == "__main__":
    result = find_src_openeuler_dirs(".")
    name = find_sig_dirs(result)
