<?php

echo '<!DOCTYPE html>

<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!--meta http-equiv="refresh" content="60"-->
  <title>Heart Disease Predictor</title>
  <link rel="stylesheet" type="text/css" href="../static/style.css">
  <script src="https://kit.fontawesome.com/5f3f547070.js" crossorigin="anonymous"></script>
  <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
</head>

<body>

  <!-- Website Title -->

  <div class="container">
    <h2 class="container-heading"><span class="heading_font">Heart Disease Predictor</span></h2>
    <div class="description">
    <image  class="image1" src="../static/heart1.png" alt="pic1"> 
      <p>A Machine Learning based Web Application that Digitization and Predict of having heart Disease or not by ECG paper, Built with Flask and Deploy using Heroku.</p><br>
        <p>(Note:This model is 97.41% accurate)</p>
    </div>
  </div>

  <!-- Text Area -->
  <div class="ml-container">
    <form action="http://localhost:5000/result" method="POST">
     

        <p>Upload ECG image:<input type="file" name="file"  placeholder="Select ECG image" required="required" accept="image/*"  onchange="validateFileType()"/>
<script type="text/javascript">
    function validateFileType(){
        var fileName = document.getElementById("fileName").value;
        var idxDot = fileName.lastIndexOf(".") + 1;
        var extFile = fileName.substr(idxDot, fileName.length).toLowerCase();
        if (extFile=="jpg" || extFile=="jpeg" || extFile=="png"){
            //TO DO
        }else{
            alert("Only jpg/jpeg and png files are allowed!");
        }   
    }
</script><br></p>
     <!--p><font face = "WildWest" size = "3"> <i>Input number of record in dataset</i></font--></p--><!-- p><input type="text" name="text></p-->
        

      <input type="submit" class="my-cta-button" value="Predict">
       
    </form>
   
    
  </div>

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
?>

