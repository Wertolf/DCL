def thisORthat(actual_path):
    import os, sys
    cwd = os.getcwd()
    print(cwd)
    print(actual_path)
    return cwd in actual_path

    # 替代方案
    '''
    unknown_path = os.path.join(cwd, r'Modules\Classes\Text.py')
    if (not os.path.lexists(unknown_path)) or \
       (not os.path.samefile(actual_path, unknown_path)):
        print('hello')
    else:
        sys.stderr.write('byg')
    '''

thisORthat(r'G:\Users\Wert Yu\Documents\GitHub\DCL\Modules\Classes\Text.py')
