<?php

echo' <!DOCTYPE html>

<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Security-Policy" content="font-src "self" data:; img-src "self" data:; 
    default-src "self" http://localhost:5000/">
  <title>Heart Disease Predictor</title>
  <link rel="stylesheet" type="text/css" href="../static/style1.css">
  <script src="https://kit.fontawesome.com/5f3f547070.js" crossorigin="anonymous"></script>
  <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
  <!--meta http-equiv="refresh" content="60"-->
  

<script lang="javascript">
    window.onload = function() {
	if(!window.location.hash) {
		window.location = window.location + "#loaded";
		window.location.reload();
	    }
        }
 </script>
    
</head>

<body>



        <!-- Website Title -->
	<div class="container">
            <image  class="image1" src="../static/heart.jpg" alt="pic1"> 
                <h2 class="container-heading"><span class="heading_font">Heart Disease Predictor</span></h2>
                
                <br><p>A Machine Learning Web App, Built with Flask, Deployed using Heroku.</p>
    		
               
    	</div>
      

		<!-- Result -->
		<div class="results">
                {% if hr>=1 %}
                    <h1>average of  heart rate is.<font face = "WildWest" size = "5" color=red><u>{{hr}}</u></font></h1>
                     {% endif %}
			{% if prediction==1 %}
				<h1>Prediction: <span class="danger">Oops! You have "Premature Atrial Contractions" Heart Disease.Type 1</span></h1><br>
                                For Further Information <a href="https://www.webmd.com/heart-disease/atrial-fibrillation/premature-atrial-contractions">Click here</a>
				
			{% elif prediction==0 %}
				<h1>Prediction: <span class="safe">Great! You DONT  have Heart Disease.Normal</span></h1>
                                
                                 
			{% elif prediction==2 %}
				<h1>Prediction: <span class="danger">Oops! You have  "Premature Ventricular Contraction" Heart Disease.Type 2</span></h1><br>
                                For Further Information <a href="https://my.clevelandclinic.org/health/diseases/17381-premature-ventricular-contractions">Click here</a>
			        
                        {% elif prediction==3 %}
				<h1>Prediction: <span class="danger">Oops! You have  "Fusion of ventricular" Heart Disease.Type 3</span></h1><br>
                                For Further Information <a href="https://litfl.com/fusion-beat-dressler-beat-ecg-library/">Click here</a>
                        
                        {% elif prediction==4 %}
				<h1>Prediction: <span class="danger">Oops! You have Fusion of paced  Heart Disease.Type 4</span></h1>
                                <br>For Further Information <a href="https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/fusion-beat">Click here</a>
                        {% endif %}
                        <br><br><br>
                         <b><a href="../myfile2.csv" download="w3logo"> download digitization of ECG paper
  
                         </a></b>
                       
                       
                       <image class="graph" src="../static/QRS_pks.png" alt="pic1">
                        
		</div>
              <div class="b1">  <form>
 <input type="button" value="Go back!" onclick="history.back()">
</form></div>
                

		<!-- Footer -->
  <div class="footer">
    <div class="contact">
      <a target="_blank" href="https://github.com/asthasharma98/Heart-Disease-Prediction-Deployment"><i
          class="fab fa-github fa-lg contact-icon"></i></a>
      <a target="_blank" href="https://www.linkedin.com/in/astha-sharma-47266b11b/"><i
          class="fab fa-linkedin fa-lg contact-icon"></i></a>
    </div>
    <p class="footer-description">Made by Ibraheam Fathail.</p>
  </div>


	</body>
</html>
';

