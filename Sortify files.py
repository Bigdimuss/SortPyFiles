#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import shutil

formats = {
    'Videos':[
        '.3g2',
        '.3gp',
        '.asf',
        '.avi',
        '.f4v',
        '.flv',
        '.m2t',
        '.m2ts',
        '.m2v',
        '.m4v',
        '.mjpeg',
        '.mkv',
        '.mk3d',
        '.mka',
        '.mks',
        '.mov',
        '.qt',
        '.mp4',
        '.mpg',
        '.mpeg',
        '.mts',
        '.m2ts',
        '.mxf',
        '.ogv',
        '.rm',
        '.swf',
        '.ts',
        '.vob',
        '.webm',
        '.wmv',
        '.mtv',
        ],
    'Music':[
        '.aac', 
        '.m4a',
        '.m4p',
        '.m4b',
        '.ac3',
        '.aif',
        '.aifc',
        '.aiff',
        '.aif',
        '.au',
        '.caf',
        '.dts',
        '.flac',
        '.gsm',
        '.m4a',
        '.m4b',
        '.m4r',
        '.mmf',
        '.mp2',
        '.mp3',
        '.mpa',
        '.oga',
        '.ogg',
        '.opus',
        '.ra',
        '.ram',
        '.snd',
        '.voc',
        '.wav',
        '.wave',
        '.wma',
        ],
    'Pictures':[
        '.jpg',
        '.jpeg',
        '.jpe',
        '.jif',
        '.jfif',
        '.jfi',
        '.png',
        '.gif',
        '.webp', 
        '.tiff',
        '.tif', 
        '.raw', 
        '.arw', 
        '.cr2', 
        '.nrw', 
        '.k25',
        '.bmp',
        '.dib',
        '.heif', 
        '.heic',
        '.jp2', 
        '.j2k', 
        '.jpf', 
        '.jpx', 
        '.jpm', 
        '.mj2',
        '.ico',
        ],
    'Graphism':[
        '.psd', 
        '.ind', 
        '.indd',
        '.indt', 
        '.psd', 
        '.svg', 
        '.svgz', 
        '.ai', 
        '.eps',
        '.xcf',
        '.pat',
        '.gbr',
        '.sun',
        '.bm',
        '.dcm',
        '.sla',
        ],
    '3D':[
        '.obj',
        '.blend',
        '.blend1',
        '.usd',
        '.usdc',
        '.usda',
        '.abc',
        '.ply'
        ],
    'Documents':[
        '.pdf',
        '.doc',
        '.docx',
        '.odt',
        '.xls',
        '.xlsx',
        '.ods',
        '.odp',
        '.odg',
        '.ppt',
        '.pptx',
        '.txt',
        ],
    'Archives':[
        '.7z',
        '.s7z',
        '.ace',
        '.afa',
        '.alz',
        '.arc',
        '.ark',
        '.zip', 
        '.zipx',
        '.tar.gz',
        '.gz',
        '.xz'
        '.tgz',
        '.tar.Z',
        '.tar.bz2',
        '.tar',
        '.tbz2',
        '.tar.lz',
        '.tlz', 
        '.tar.xz',
        '.txz',
        '.tar.zst',
        '.rar'
    ],
    'PixelArt':['.pxo','.ase','.asprite'],
    'Programming':[
        '.php',
        '.py', 
        '.html',
        '.xml',
        '.htm',
        '.csv', 
        '.db',
        '.jar',
        '.json'],
    'Torrents':['.torrent',],
    'Iso':['.iso',],
    'Windows':['.exe',],
    'Messy Folder':None,
    'Templates':None,
    'Public':None,
    'Downloads':None,
    'Desktop':None,

    
}

def get_file_type(ext:str):
    for value in formats:
        if ext.lower() in formats[value]:
            return value
    return None
            
fichiers = sys.argv[1:]
directories = formats.keys()

for value in fichiers:
    if os.path.isfile(value):
        try:
            f = os.path.splitext(value)
            print(f)
            dir_name = get_file_type(f[1])
            print(dir_name)
            if dir_name != None:
                if not os.path.exists(dir_name):
                    os.mkdir(dir_name)
                shutil.move(value, dir_name+'/'+value)
            else:
                shutil.move(value, 'Messy Folder/'+value)
        except:
            continue
    if os.path.isdir(value):
        try:
            if value not in directories:
                shutil.move(value,'Messy Folder'+'/'+value)
        except:
            continue

