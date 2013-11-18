__author__ = 'Administrator'
#__*__ coding=utf-8 __*__
#import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element,ElementTree
def read_xml(in_path):
    #读取并解析xml文件
    #in_path:xml路径
    #return:ElementTree
    tree = ElementTree()
    tree.parse(in_path)
    return tree
#    print tree
def write_xml(tree,out_path):
    '''将xml文件写出
    tree:xml树
    out_path:写出路径'''
#    tree = ElementTree()
    tree.write(out_path,encoding="utf-8",xml_declaration=True)
def if_match(node,kv_map):
    '''判断某个节点是否包含所有传入参数属性
    node:节点
    kv_map:属性及属性值组成的map
    '''
    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
        return True
def find_nodes(tree,path):
    '''查找路径匹配的所有节点
    tree:xml树
    path:节点路径'''
    return tree.findall(path)
 #   print tree.findall(path)

def get_node_by_keyvalue(nodelist,kv_map):
    '''根据属性和属性值定位符合的节点，返回节点
    nodelist:节点列表
    kv_map:匹配属性和属性值的map'''
    result_nodes = []
    for node in nodelist:
        if if_match(node,kv_map):
            result_nodes.append(node)
    return result_nodes

def change_node_text(nodelist,text,is_add=False,is_delete=False):
    '''改变/增加/删除一个节点的文本
    nodelist:节点列表
    text:更新后的文本
    '''
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
            node.text = ""
        else:
            node.text = text


tree = read_xml('./movies.xml')
#print  tree.find('./type')
#node = tree.find('./type')
#node.text = "win7"
#text_nodes = get_node_by_keyvalue(find_nodes(tree,"movie"),{"title":"Enemy Behind"})
text_nodes = tree.findall('movie/type')
print text_nodes
change_node_text(text_nodes,"honggaoliang")

write_xml(tree,"./out.xml")
find_nodes(tree,"movie/type")
