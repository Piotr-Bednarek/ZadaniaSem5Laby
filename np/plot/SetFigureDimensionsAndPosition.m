function SetFigureDimensionsAndPosition(figVector,figureXsize,figureYsize)

figureXzero = 1500-figureXsize; figureYzero = 750-figureYsize; 
if length(figVector)==1
    figVector.Position = [figureXzero figureYzero figureXsize figureYsize];
else
   switch length(figVector)
       case 2
          figVector(1).Position = [figureXzero figureYzero figureXsize figureYsize];
          figVector(2).Position = [figureXzero figureYzero-figureYsize-83 figureXsize figureYsize];
       case 3
          figureXzero = 1500-2*figureXsize;
          figVector(1).Position = [figureXzero figureYzero figureXsize figureYsize];
          figVector(2).Position = [figureXzero figureYzero-(figureYsize+83) figureXsize figureYsize];
          figVector(3).Position = [figureXzero+figureXsize figureYzero figureXsize figureYsize];
          %figVector(3).Position = [figureXzero figureYzero-2*(figureYsize+83) figureXsize figureYsize];
       case 4
          figureXzero = 1500-2*figureXsize;
          figVector(1).Position = [figureXzero figureYzero figureXsize figureYsize];
          figVector(2).Position = [figureXzero figureYzero-(figureYsize+83) figureXsize figureYsize];
          figVector(3).Position = [figureXzero+figureXsize figureYzero figureXsize figureYsize];
          figVector(4).Position = [figureXzero+figureXsize figureYzero-(figureYsize+83) figureXsize figureYsize];
 
   end
end

end

