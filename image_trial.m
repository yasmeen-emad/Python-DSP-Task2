% Read the images in   
%Image1=double(imread('1.png'))/255;
%Image2=double(imread('2.bmp'))/255;

Image1 = im2double(imread('1.tif'));
load mandrill;
clear caption;
Image2 = X / 255; clear X;
Image2 = imresize(Image2, 0.5, 'bilinear');

% Find dimensions and extent of the FFT
[rows1, cols1] = size(Image1);
[rows2, cols2] = size(Image2);

rows = max(rows1, rows2);
cols = max(cols1, cols2);

% Take the FFT
Image1_FFT=fft2(Image1, rows, cols);
Image2_FFT=fft2(Image2, rows, cols);

% NEW - Find the magnitudes and phase responses
mag1 = abs(Image1_FFT);
mag2 = abs(Image2_FFT);
pha1 = angle(Image1_FFT);
pha2 = angle(Image2_FFT);

% Recompute frequency responses by swapping the phases
out1 = mag1 .* exp(j*pha2);
out2 = mag2 .* exp(j*pha1);

% Find the inverse images
out1 = real(ifft2(out1));
out2 = real(ifft2(out2));

% Show the images
figure;
imshow(out1, []);
figure;
imshow(out2, []);