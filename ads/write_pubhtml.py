#!/usr/bin/env python
"""
-- shamelessly stolen from Mike Zingale
"""
import parser

# Read in paper and presentation bibliographies 
papers = parser.parse_bibfile("papers.bib")
pres = parser.parse_bibfile("presentations.bib")

# Print Titles of Papers and Presentations on website 
print("\nPAPERS\n")
for p in papers: print(p)

print("\nPRES\n")
for pr in pres: print(pr)

# sorted by date
tf = open("pub_template.html", "r")
dh = open("publications-and-pres.html", "w")

### ---------------------------------------------- ###
### ------------ Iterate over Papers ------------- ###
### ---------------------------------------------- ###

# Set initial parameters to pull out years 
current_year = 0
first = True
papers_list = ""

# Loop over papers
for p in papers:
    if not first: papers_list += "</dl>\n"
    else: first = False

    papers_list += "<p><h2><a name='{}'></a>{}</h2>\n\n".format(p.year, p.year)
    papers_list += "<dl>\n"

    current_year = p.year

    t, o, l = p.jstring()
    if not l == "": papers_list += "<dt><a href='{}'>{}</a></dt>\n".format(l, t)
    else: papers_list += "<dt>{}</dt>\n".format(t)

    papers_list += "<dd>{}</dd>\n\n".format(o)

papers_list += "</dl>\n\n"

### ---------------------------------------------- ###
### -------- Iterate over Presentations ---------- ###
### ---------------------------------------------- ###

# Reset initial parameters to pull out years 
current_year = 0
first = True
pres_list = ""

# Loop over presentations 
for pr in pres:
    if not first: pres_list += "</dl>\n"
    else: first = False

    pres_list += "<p><h2><a name='{}'></a>{}</h2>\n\n".format(pr.year, pr.year)
    pres_list += "<dl>\n"

    current_year = pr.year

    t, o, l = pr.jstring()
    if not l == "": pres_list += "<dt><a href='{}'>{}</a></dt>\n".format(l, t)
    else: pres_list += "<dt>{}</dt>\n".format(t)

    pres_list += "<dd>{}</dd>\n\n".format(o)

pres_list += "</dl>\n\n"

### ---------------------------------------------- ###
### ---------- Write to html and close  ---------- ###
### ---------------------------------------------- ###

for line in tf:
    dh.write(line.replace("@@pub-list@@", papers_list).replace("@@pres-list@@", pres_list).replace("permalink: /pubs", "permalink: /publications-and-pres")) #.replace("@@year-index@@", year_index).replace("@@sub-index@@", "")

dh.close()
tf.close()










# by year
# years = list(set([p.year for p in papers])) + list(set([pr.year for pr in pres]))
# years.sort(reverse=True)

# print(years)

# year_index = "<ul>\n"
# for n, y in enumerate(years):
#     if n % 3 == 0:
#         year_index += "<li>"
#     else:
#         year_index += "&nbsp;&nbsp;&nbsp;"

#     year_index += "<a href='#{}'>{}</a>".format(y, y)

#     if n % 3 == 2:
#         year_index += "</li>\n"

# if not len(year_index) % 3 == 0: 
#     year_index += "</li>\n"

# year_index += "</ul>\n"


# year_index = "<ul>\n"
# for n, y in enumerate(years):
#     if n % 3 == 0:
#         year_index += "<li>"
#     else:
#         year_index += "&nbsp;&nbsp;&nbsp;"

#     year_index += "<a href='#{}'>{}</a>".format(y, y)

#     if n % 3 == 2:
#         year_index += "</li>\n"

# if not len(year_index) % 3 == 0: 
#     year_index += "</li>\n"

# year_index += "</ul>\n"



# # by subject
# tf = open("pub_template.html", "r")
# dh = open("publications-by-topic.html", "w")

# subs = list(set([p.subject for p in papers]))
# subs.sort(key=str.lower)

# papers_by_subj = {}

# for p in papers:
#     subj = p.subject
#     if not subj in papers_by_subj.keys():
#         papers_by_subj[subj] = [p]
#     else:
#         papers_by_subj[subj].append(p)

# sub_index = "<ul>\n"
# for s in subs:
#     sub_index += "<li><a href='#{}'>{}</a></li>\n".format(s.replace(" ", "_").replace(":", ""), s)
# sub_index += "</ul>\n"


# # now loop over subject
# papers_list = ""
# for s in sorted(papers_by_subj, key=str.lower):
#     ps = papers_by_subj[s]
#     ps.sort(reverse=True)

#     papers_list += "<p><h2><a name='{}'></a>{}</h2>\n".format(s.replace(" ", "_").replace(":", ""), s)
#     papers_list += "<dl>\n"

#     for p in ps:

#         t, o, l = p.jstring()
#         if not l == "":
#             papers_list += "<dt><a href='{}'>{}</a></dt>\n".format(l, t)
#         else:
#             papers_list += "<dt>{}</dt>\n".format(t)

#         papers_list += "<dd>{}</dd>\n".format(o)

#     papers_list += "</dl>\n"

# for line in tf:
#     dh.write(line.replace("@@pub-list@@", papers_list).replace("@@year-index@@", "").replace("@@sub-index@@", sub_index),replace("permalink: /pubs", "permalink: /publications-by-topic"))

# dh.close()
# tf.close()

