import streamlit as st
from pyvis.network import Network

# Person Class (as before)
class Person:
    def __init__(self, name, spouse=None, children=None):
        self.name = name
        self.spouse = spouse
        self.children = children or []

# Create family members
homer = Person("Homer Simpson")
marge = Person("Marge Simpson")
bart = Person("Bart Simpson")
lisa = Person("Lisa Simpson")
maggie = Person("Maggie Simpson")

# Establish relationships
homer.spouse = marge
marge.spouse = homer
homer.children = [bart, lisa, maggie]
marge.children = [bart, lisa, maggie]

# Print family tree (rudimentary representation)
#print("Homer Simpson")
#print("Spouse:", homer.spouse.name)
#print("Children:", [child.name for child in homer.children])

# UI Components
st.title("Simpsons Family Tree")

selected_person_name = st.selectbox("Select a person", [homer.name, marge.name, bart.name, lisa.name, maggie.name])

# Visualization using pyvis
def build_tree_pyvis(name):
    net = Network(notebook=True)
    def add_node_and_children(name, parent=None):
        net.add_node(name)
        if parent:
            net.add_edge(parent, name)
        person = next((p for p in [homer, marge, bart, lisa, maggie] if p.name == name), None)
        if person:
            for child in person.children:
                add_node_and_children(child.name, name)
    add_node_and_children(selected_person_name)
    return net

net = build_tree_pyvis(selected_person_name)
try:
    path = '/tmp'
    net.save_graph(f'{path}/pyvis_graph.html')
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 900)
except:
    st.error("An error occurred while generating the network graph.")
