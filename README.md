# Isse playground

Experiment with the [hub](https://github.com/github/hub) tool to manage github issues.

Use repo:
```
https://github.com/cwebber314/project_test
```

Create issues:
```
hub issue create -a cwebber314 -l example_label -F example_issue.txt
```

## Create issues from a spreadsheet

First create the issue text files:
```
python create_files.py
```

Then create the list of hub commands:
```
python make_issues.py
```

Inspect ``make_issues.bat`` check the syntax.  Run the bat file to create the issues.  
```
.\make_issues.bat
```

You can check github to make sure the issues were created:
```
hub issue -- browse
```
