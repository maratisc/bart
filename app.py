import streamlit as st
import json

# ... (Person class and family data as before)
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

st.title("Simpson Family Tree")

#selected_person_name = st.selectbox("Select a person", [homer.name, marge.name, bart.name, lisa.name, maggie.name])
selected_person_name = homer.name

# Convert family data to JSON
def convert_to_json(name):
    data = []
    def add_node_and_children(name, parent=None):
        node = {"name": name}
        if parent:
            node["parent"] = parent
        data.append(node)
        person = next((p for p in [homer, marge, bart, lisa, maggie] if p.name == name), None)
        if person:
            for child in person.children:
                add_node_and_children(child.name, name)
    add_node_and_children(selected_person_name)
    return json.dumps(data)

family_data_json = convert_to_json(selected_person_name)
#print("family_data_json:", family_data_json)

# Read HTML file
#with open("tree.html", "r") as f:
#    html_content = f.read()
    
# Embed JSON data in HTML
#html_content = f"var familyData = {family_data_json};\n" + html_content

# Display HTML with D3
st.components.v1.html(
    '''<script>var familyData = {family_data_json};</script>'''
)
