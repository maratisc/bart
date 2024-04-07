import streamlit as st
import networkx as nx

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

selected_person = st.selectbox("Select a person", [homer, marge, bart, lisa, maggie])
# ... (display selected person's details)

# Visualization using NetworkX
def build_tree_nx(person):
    G = nx.DiGraph()
    def add_node_and_children(person, parent=None):
        G.add_node(person.name)
        if parent:
            G.add_edge(parent.name, person.name)
        for child in person.children:
            add_node_and_children(child, person)
    add_node_and_children(selected_person)
    return G

graph = build_tree_nx(selected_person)
st.graphviz_chart(nx.nx_agraph.to_agraph(graph))