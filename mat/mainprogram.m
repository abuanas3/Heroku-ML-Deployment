clc; clear; close all; warning off all;

rgb1 = imread('geeks.jpg');

hasil_crop = imcrop(rgb1); %hasil crop disimpan

%dlmwrite('myfile.csv',hasil_crop)
%imwrite(hasil_crop,'hasil_crop.jpg');
imwrite(hasil_crop,'hasil_crop.jpg');
[BW,rgb] = createMaskbr(hasil_crop);


bw4 = bwareaopen(BW,1260);
figure, imshow(hasil_crop);

imbwaa=flip(bw4 ,1); %# vertical flip 
[ k ] = thinning( imbwaa );
%run deteksi_tepi.m 
run digitasi;
%dlmwrite('myfile8.csv',HASIL_AKHIRAVF);
