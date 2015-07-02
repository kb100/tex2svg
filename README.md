Looks for math tags in an html source and replaces their LaTeX source contents with statically compiled inline base 64 encoded svgs.

Requirements: python3, pdflatex, pdfcrop, pdf2svg, base64

Advantages over MathJax: no javascript required, images are statically compiled ahead of time.

Disadvantages: it doesn't work yet. I don't know how to automatically determine the height and padding of the generated svgs. Presently you can manually change the height and padding to make things line up. Feel free to contribute if you know how to solve these problems.

The file `exampleOut.html` was created from `exampleIn.html` from running
    
    ./htmlsub.py exampleIn.html exampleOut.html
