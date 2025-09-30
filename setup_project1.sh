# Use mkdir -p to create directories
mkdir -p src data output

# Create Python templates with function stubs and TODO comments
echo "#TODO: Implement analysis here" > src/data_analysis.py
echo "Setting up data_analysis.py"
echo "#TODO: Add functions for data analysis here" > src/data_analysis_functions.py
echo "Setting up data_analysis_functions.py"

# Use here-documents (cat > filename << 'EOF') to create files
cat > data/students.csv << 'EOF'
name,age,grade,subject
John,20,90,Biology
Jane,22,95,Math
Bob,19,85,Physics
Yvonne,20,99,Biology
Roxi,21,96,Environmental_Science
Marcus,23,93,Math
Harley,20,91,English
Julian,20,98,Linguistics
EOF
# Create a CSV file with student data (name,age,grade,subject)
echo "Setting up students.csv"

echo "TODO#setup gitignore" > output/.gitignore
echo ".gitignore" >> output/.gitignore
echo "TODO# setup requirements.txt" > output/requirements.txt
echo "requirements.txt" >> output/requirements.txt