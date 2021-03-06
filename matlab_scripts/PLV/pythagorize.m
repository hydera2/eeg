function pyth = pythagorize(x)
    d1 = (sqrt(((x(:,1).^2)+(x(:,2).^2)+(x(:,3).^2))/3));
    d2 = (sqrt(((x(:,4).^2)+(x(:,5).^2)+(x(:,6).^2))/3));
    d3 = (sqrt(((x(:,7).^2)+(x(:,8).^2)+(x(:,9).^2))/3));
    d4 = (sqrt(((x(:,10).^2)+(x(:,11).^2)+(x(:,12).^2))/3));
    d5 = (sqrt(((x(:,13).^2)+(x(:,14).^2)+(x(:,15).^2))/3));
    d6 = (sqrt(((x(:,16).^2)+(x(:,17).^2)+(x(:,18).^2))/3));
    d7 = (sqrt(((x(:,19).^2)+(x(:,20).^2)+(x(:,21).^2))/3));
    d8 = (sqrt(((x(:,22).^2)+(x(:,23).^2)+(x(:,24).^2))/3));
    d9 = (sqrt(((x(:,25).^2)+(x(:,26).^2)+(x(:,27).^2))/3));
    d10 = (sqrt(((x(:,28).^2)+(x(:,29).^2)+(x(:,30).^2))/3));
    d11 = (sqrt(((x(:,31).^2)+(x(:,32).^2)+(x(:,33).^2))/3));
    d12 = (sqrt(((x(:,34).^2)+(x(:,35).^2)+(x(:,36).^2))/3));
    d13 = (sqrt(((x(:,37).^2)+(x(:,38).^2)+(x(:,39).^2))/3));
    d14 = (sqrt(((x(:,40).^2)+(x(:,41).^2)+(x(:,42).^2))/3));
    d15 = (sqrt(((x(:,43).^2)+(x(:,44).^2)+(x(:,45).^2))/3));
    evar = horzcat(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15); 
    pyth = evar;
end
