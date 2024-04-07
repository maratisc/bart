import streamlit as st
from streamlit_agraph import agraph, Node, Edge

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

# Visualization using streamlit-agraph
nodes = []
edges = []

def build_tree(name, parent_id=None):
    node_id = name
    nodes.append(Node(id=node_id, label=name))
    if parent_id:
        edges.append(Edge(source=parent_id, target=node_id))
    person = next((p for p in [homer, marge, bart, lisa, maggie] if p.name == name), None)
    if person:
        for child in person.children:
            build_tree(child.name, node_id)

build_tree(selected_person_name)

config = {
    "width": 800,
    "height": 600,
    "directed": True,
    "nodeHighlightBehavior": True,
}

agraph(nodes=nodes, edges=edges, config=config)