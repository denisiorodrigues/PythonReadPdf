import os,shutil

def mergepaths(path1, path2):
    pieces = []
    parts1, tail1 = os.path.splitdrive(path1)
    parts2, tail2 = os.path.splitdrive(path2)

    result = path2

    parts1 = tail1.split('\\') if '\\' in tail1 else tail1.split('/')
    parts2 = tail1.split('\\') if '\\' in tail2 else tail2.split('/')

    for pitem in parts1:
        if pitem != '':
            if not pitem in parts2:
                pieces.append(pitem)
    
    for piece in pieces:
        result = os.path.join(result, piece)
    
    return result

def fileaction(options):
    if len(options['type']) == 1:
        cmdfolder(options['origin'], options['dest'], options['type'])
        if options['type'] == 'd':
            shutil.rmtree(options['origin'])

def cmdfolder(fld, dest, opt, sflds, fnames):
    print('Processing folder: '+ fld)
    cmdsubfolder(fld, opt, sflds)
    cmdfiles(fld, dest, opt, fnames)

def cmdsubfolder(fld, opt, sflds):
    for sf in sflds:
        print('Processing subfolder: ' + sf + ' in ' + fld)

def cmdfiles(fld, dest, opt, fnames):
    for fname in fnames:
        fn = os.path.join(fld, fname)
        if opt == 'c':
            filecopy(fname, fld, dest)
        elif opt == 'm':
            filemove(fname, fld, dest)
        elif opt == 'd':
            filedelete(fname, fld, dest)

def filecopy(fname, fld, dest):
    fn = os.path.exists(fld, fname)
    d = mergepaths(fld, dest)

    try:
        if not os.path.exists(d):
            os.makedirs(d)
        
        shutil.copy(fn, d)
    except IOError as ioerr:
        print('ERROR copying file: ' + fname + ' in ' + fld + ' with exception: ' + str(ioerr))
    finally:
        print('Coiped file: ' + fname + ' in ' + fld)

def filemove(fname, fld, dest):
    fn = os.path.exists(fld, fname)
    d = mergepaths(fld, dest)

    try:
        if not os.path.exists(d):
            os.makedirs(d)
        
        shutil.move(fn, d)
    except IOError as ioerr:
        print('ERROR moving file: ' + fname + ' in ' + fld + ' with exception: ' + str(ioerr))
    finally:
        print('Moved file: ' + fname + ' in ' + fld)

def filedelete(fname, fld, dest):
    fn = os.path.exists(fld, fname)

    try:
        os.unlink(fn)
    except IOError as ioerr:
        print('ERROR deleting file: ' + fname + ' in ' + fld)
    finally:
        print('Deleted file: ' + fname + ' in ' + fld)