#!/usr/bin/env python3
import os
import sys
import binascii

def encode(filename):
    basename = os.path.basename(filename)
    try:
        # 以二进制模式读取文件
        with open(filename, 'rb') as f:
            content = f.read()
            # 使用binascii.hexlify将二进制数据转换为十六进制字符串
            hex_content = binascii.hexlify(content).decode('ascii')
            
            # 生成JavaScript代码
            js_content = 'fmj.rom["%s"] = "%s";\n' % (basename, hex_content.upper())
            
            # 写入.js文件
            js_filename = filename + '.js'
            with open(js_filename, 'w') as f:
                f.write(js_content)
                
            print('Successfully processed: %s -> %s' % (filename, js_filename))
            
    except IOError as e:
        print('Error reading file %s: %s' % (filename, str(e)))
        sys.exit(1)
    except Exception as e:
        print('Unexpected error: %s' % str(e))
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print('Usage: %s <file1> [file2] [file3] ...' % sys.argv[0])
        sys.exit(1)
    
    for filename in sys.argv[1:]:
        if not os.path.exists(filename):
            print('Error: File not found: %s' % filename)
            sys.exit(1)
        print('Encoding %s' % filename)
        encode(filename)

if __name__ == '__main__':
    main()