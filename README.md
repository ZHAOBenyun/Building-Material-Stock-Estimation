<h1 style="text-align: center; font-size: 35px; font-family: 'Sama Devanagari';"> Building Material Stock Estimation Method
</h1>

<h3 style="text-align: center; font-size: 28px; font-family: 'Sama Devanagari';"> 
Autonomous Building Material Stock Estimation Using 3D Modeling and Multilayer Perceptron: A Case of Hong Kong
</h3>



<div style=" text-align: center; font-size: 21px;">
Qingxiang Li<sup>1</sup>, Benyun Zhao<sup>1</sup>, Xinyi Wang<sup>1</sup>, Guidong Yang<sup>1</sup>, Yuyang Chang<sup>2</sup>, Xi Chen<sup>1</sup>, and <br> <a href="http://www.mae.cuhk.edu.hk/~bmchen/">Ben M. Chen</a><sup>1</sup>
</div>
<div  style="text-align: center; font-size: 18px;" >
1.Department of Mechanical and Automation Engineering, The Chinese University of Hong Kong <br>   
2.Ecosystem Management, Department of Environmental System Sciences, ETH Zurich
</div>



<!-- <br>
<button style="background-color: #000000; color: white; margin: 0 auto; padding: 10px 15px;border: none; border-radius: 5px;">
Dataset can be available at: <br><a href="https://mycuhk-my.sharepoint.com/:f:/g/personal/1155145791_link_cuhk_edu_hk/EvIGO4s7idhAuIj_WrfJ3wgB5HS6bSfPbce8WJxqLEwEWA?e=ftelDM" style="color: white; text-decoration: none;">https://mycuhk-my.sharepoint.com/:f:/g/personal/1155145791_link_cuhk_edu_hk/EvIGO4s7idhAuIj_WrfJ3wgB5HS6bSfPbce8WJxqLEwEWA?e=ftelDM</a>
</button> -->


<div style="text-align: left; font-family: 'American Typewriter'; font-weight: 400; font-size:15px"> 
<h2>Abstract</h2>
</div>
Building material stock (BMS) modeling is crucial to promote circular economy practices in urban environment. This study presents a fully autonomous bottom-up approach for BMS estimation using 3D Modeling and Multilayer Perceptron (MLP). Firstly, an archetype-based MLP model for concrete and steel stock prediction is developed and trained using the feature information collected from Building Information Modeling of local buildings, with an 89.9% estimation accuracy in the best performance. A novel 3D modeling workflow is developed using an innovative point cloud reconstruction method, in order to create editable 3D building models. These models facilitate the extraction of key building features, which are then inputted into pre-trained MLP models to estimate the BMS. The approach is tested in three experiments at varying scales, individual buildings, districts, and urban areas, demonstrating its effectiveness and scalability for large-scale BMS estimation. As a case study, concrete and steel stocks for above-ground buildings in Hong Kong are quantified at a 500-meter resolution. The bottom-up methodology allows for a more precise assessment of material composition, intensity, and geographic distribution, offering crucial insights for resource management. In summary, this study is a pioneering effort in automating the BMS estimation process, addressing critical issues of data accessibility, accuracy, and scalability while contributing to the broader goals of sustainable construction and resource management.

<div style="text-align: left; font-family: 'American Typewriter'; font-weight: 400; font-size:15px"> 
<h2>MLP for Prediction</h2>
</div>
The MLP model is trained using the feature information collected from Building Information Modeling of local buildings. The model is trained using the following features, and method is demonstrated in the <a href="./building_predict.py" style="color: white; text-decoration: none;">python file</a>


<p align="center">
  <img src="./mlp.png" width=80% height=80%> 
</p>

<div style="text-align: center; font-family: 'American Typewriter'; font-weight: 400; "> 
<h2>Acknowledgement</h2>
</div>
This work was supported by the InnoHK of the Government of the Hong Kong Special Administrative Region via the Hong Kong Centre for Logistics Robotics. 

