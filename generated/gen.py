# -*- coding: utf-8 -*-
import os
name = "1800-Talet Historia"
image = "https://merchantsandmechanics.files.wordpress.com/2017/12/manchester-2.jpg?w=900"

htmlDoc = ("""
<!DOCTYPE html>

<html lang="sv">
	<head>
		<!-- Meta -->
		<meta charset="UTF-8" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="description" content="Aaron Clauss Egna Fina Hemgjorda Hemsida Som Tog Tårar Och Svett Och Halva Mitt Sommarlov För Att Skapa Så Du Måste Så Klart Gilla Den, Eller Hur?">
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<!-- Scripts -->
		<script defer src="../scripts/header.js"></script>
		<!-- Links -->
		<link rel="stylesheet" href="../style/style.css" />
		<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,700&display=swap"/>
		<link rel="icon" href="../images/icon.ico">
		<!-- Title -->
		<title>""" + name + """ | Kanaron</title>
	</head>
	
	<body>
		<header id="header">
			<a href="../index.html" class="logo">kanaron</a>
			<nav>
				<ul class="nav-links">
					<!-- <li><a class="active" href="#">Startsida</a></li> -->
					<li><a href="../about.html">Om Sidan</a></li>
					<li><a href="../vanlig.html">Vanlig Stad</a></li>
					<li><a class="active" href="articles.html">Artiklar</a></li>
				</ul>
			</nav>
			<button id="theme-toggle" aria-label="Switch to dark theme">
				<svg xmlns="http://www.w3.org/2000/svg" width="472.39" height="472.39" viewBox="0 0 472.39 472.39">
					<g class="toggle-sun">
						<path d="M403.21,167V69.18H305.38L236.2,0,167,69.18H69.18V167L0,236.2l69.18,69.18v97.83H167l69.18,69.18,69.18-69.18h97.83V305.38l69.18-69.18Zm-167,198.17a129,129,0,1,1,129-129A129,129,0,0,1,236.2,365.19Z" />
					</g>
					<g class="toggle-circle">
						<circle class="cls-1" cx="236.2" cy="236.2" r="103.78" />
					</g>
				</svg>
			</button>
			<p class="menu cta">Meny</p>
		</header>
		<div id="mobile__menu" class="overlay">
			<a class="close">&times;</a>
			<div class="overlay-content">
				<a href="../about.html">Om Sidan</a>
				<a href="../vanlig.html">Vanlig Stad</a>
				<a class="active" href="articles.html">Artiklar</a>
			</div>
		</div>

		<main>
			<section class="Hero">
				<div class="heroOverlay"></div>  
				<div class="heroImage rellax" style="background-image: url(""" + image + """);" data-rellax-speed="3"></div>
			</section>

			<!-- Place Modal if Using -->
			
			<!-- The main Article -->
			<article class="main Center">

			""","""            </article>
		</main>

		<!-- Script Libraries-->

		<!-- Rellax -->
		<script src="https://cdnjs.cloudflare.com/ajax/libs/rellax/1.12.1/rellax.min.js"></script>
		<script> 
		var rellax = new Rellax('.rellax');
		</script>

		<!-- Scroll Out -->
		<script src="https://unpkg.com/scroll-out/dist/scroll-out.min.js"></script>
		<script>ScrollOut();</script>
	</body>
</html>""")

def processString(name):
	specialChars = "!#¤%()=?$€@£{[]},*^ "
 
	for specialChar in specialChars:
		name = name.lower().replace(specialChar, "")
	name = name.replace("å", "a").replace("å","a").replace("ö","o")
	name = name.replace("&", "_").replace(".","_").replace("/", "_")

	return name



dir_path = os.path.dirname(os.path.realpath(__file__))





with open(dir_path + "\\" + processString(name) + ".html", "w", encoding="utf8") as html:
	html.write(htmlDoc[0])
	
	for line in open(dir_path + "\\index.txt", encoding="utf8"):
		if line.startswith("\\"): html.write("<section data-scroll>")
		elif line.startswith("/"): html.write("</section>")
  
		elif line.startswith("# "): html.write("<h1>" + str(line[2:-1]) + "</h1>")
		elif line.startswith("## "): html.write("<h2>" + str(line[3:-1])+ "</h2>")
		elif line.startswith("### "): html.write("<h3>" + str(line[4:-1]) + "</h3>")
		elif line.startswith("#### "): html.write("<h4>" + str(line[5:-1]) + "</h4>")
	
		elif line.startswith("*< "): html.write("<p class='italic'>" + str(line[2:-1]) + "</p>")
		elif line.startswith("*> "): html.write("<p class='italic Center'>" + str(line[2:-1]) + "</p>")

  
		elif line.startswith("\n"): html.write("<br>\n")
		# elif line.endswith("\n"): html.write(line + "<br>\n")
  
		else: 
			html.write("<p>" + str(line[:-1]) + "</p>")
			print("nu!", line)
			
    
	html.write(htmlDoc[1])


print(processString(name))