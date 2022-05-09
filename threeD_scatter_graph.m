%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%  3D scatter graphs of signal sampling using LHS %%%%%%%%%
%%%%%%  By YPE 07/04/2022 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

close all
clear
clc

source_LHS = 'Signal_Sampling_CF600';
source_TOTAL= 'TOTAL_SIGNAL_DATA_CF';
titre='LHS_Sampling';

% Read results of signal sampling
display(sprintf('Lecture du fichier %s.txt ...',source_LHS));

filename=[source_LHS,'.txt'];
fid=fopen(filename,'r');
DATA=[];

C = textscan(fid,'%f    %s    %s    %f    %f    %f');
% C = textscan(fid,'%f    %s    %s    %f    %f    %f');
% C = textscan(fid,'%f    %c    %c    %f    %f    %f','Delimiter',',');
   % for i = 1 : size(C,2)
      % DATA=[C{:,i}];
      % % DATA = [DATA C{:,i}];
   % end
% clear C;
% display(sprintf('%s read successfully !',filename));
Ca=zeros(length(C{:,1}),6);
Ca(:,1)=C{:,1};
Ca(:,4)=C{:,4};
Ca(:,5)=C{:,5};
Ca(:,6)=C{:,6};
[Cb,I]=unique(Ca,'rows');

ID=Cb(:,1);
BASIN=C{1,2}(I,1);
EVENT=C{1,3}(I,1);
PGA=Cb(:,4);
PGV=Cb(:,5);
FC=Cb(:,6);

filename=[source_TOTAL,'.txt'];
fid=fopen(filename,'r');
DATA=[];

Ct = textscan(fid,'%f    %s    %s    %f    %f    %f');
% C = textscan(fid,'%f    %s    %s    %f    %f    %f');
% C = textscan(fid,'%f    %c    %c    %f    %f    %f','Delimiter',',');
   % for i = 1 : size(C,2)
      % DATA=[C{:,i}];
      % % DATA = [DATA C{:,i}];
   % end
% clear C;
% display(sprintf('%s read successfully !',filename));

PGAt=Ct{:,4};
PGVt=Ct{:,5};
FCt=Ct{:,6};

% 1 List per basin
PGA_1 = []; PGA_2 = []; PGA_3 = [];
PGV_1 = []; PGV_2 = []; PGV_3 = [];
FC_1 = []; FC_2 = []; FC_3 = [];
index_basin1 = strfind(BASIN,'Kanto');
index_basin2 = strfind(BASIN,'Los_Angeles');
index_basin3 = strfind(BASIN,'Nagoya');


for i=1 : size(index_basin1,1)
    pos = index_basin1{i,1};
    if pos == 1
        pga_ = PGA(i); pgv_ = PGV(i); fc_ = FC(i);
        PGA_1 = [PGA_1 ; pga_]; PGV_1 = [PGV_1 ; pgv_]; FC_1 = [FC_1 ; fc_];
    end
end
    
for i=1 : size(index_basin2,1)
    pos = index_basin2{i,1};
    if pos == 1
        pga_ = PGA(i); pgv_ = PGV(i); fc_ = FC(i);
        PGA_2 = [PGA_2 ; pga_]; PGV_2 = [PGV_2 ; pgv_]; FC_2 = [FC_2 ; fc_];
    end
end

for i=1 : size(index_basin3,1)
    pos = index_basin3{i,1};
    if pos == 1
        pga_ = PGA(i); pgv_ = PGV(i); fc_ = FC(i);
        PGA_3 = [PGA_3 ; pga_]; PGV_3 = [PGV_3 ; pgv_]; FC_3 = [FC_3 ; fc_];
    end
end


figure()    
% 3D scatter graph
display (sprintf('3D scatter graph ...'));
plot3(PGAt,PGVt,FCt,'.','Markersize',20,'Color','k'); hold on
plot3(PGA,PGV,FC,'.','Markersize',20,'Color','r'); hold off

xlabel('PGA (cm/s²)')
ylabel('PGV (cm/s)')
zlabel('fc (Hz)')
grid on;
axis tight;
saveas(gcf,['3D_Scattered_',titre,'.png'])


% 3D scatter graph per basin
figure()  
display (sprintf('3D scatter graph per basin ...'));
% scat1 = plot3(PGA_1,PGV_1,FC_1,'.','Markersize',20,'Color','b','DisplayName','Basin 1');
scat1 = plot3(PGA_1,PGV_1,FC_1,'.','Markersize',20,'Color',[1 0 1],'DisplayName','Kanto');
hold on;
% scat2 = plot3(PGA_2,PGV_2,FC_2,'.','Markersize',20,'Color','r','DisplayName','Basin 2');
scat2 = plot3(PGA_2,PGV_2,FC_2,'.','Markersize',20,'Color',[0 1 1],'DisplayName','Los Angeles');
hold on;
% scat3 = plot3(PGA_3,PGV_3,FC_3,'.','Markersize',20,'Color','g','DisplayName','Basin 3');
scat3 = plot3(PGA_3,PGV_3,FC_3,'.','Markersize',20,'Color',[0.5 0.5 1],'DisplayName','Nagoya');
hold on;
legend([scat1,scat2,scat3])
xlabel('PGA (cm/s²)')
ylabel('PGV (cm/s)')
zlabel('fc (Hz)')
grid on;
axis tight;
saveas(gcf,['3D_Scattered_basin_',titre,'.png'])

figure()  
% 2D scatter graph with color map for the third variable
display (sprintf('2D scatter graph with colorbar ...'));
scatter(PGA,PGV,[],FC,'filled');
a = colorbar;
% colormap(flipud(gray));
colormap(winter);
% colormap(flipud(autumn));
xlabel('PGA (cm/s²)','FontSize',16)
ylabel('PGV (cm/s)','FontSize',16)
ylabel(a,'fc (Hz)','FontSize',16,'Rotation',90);
grid on;
axis tight;
saveas(gcf,['2D_color_Scattered_',titre,'.png'])

figure()  
% 2D scatter graph with color map for the third variable
display (sprintf('2D scatter graph with colorbar per basin ...'));
scatter(PGA,PGV,[],FC,'filled');
a = colorbar;
% colormap(flipud(gray));
colormap(winter);
% scatter(PGA_1,PGV_1,[],FC_1,'c','filled');
scatter(PGA_1,PGV_1,[],FC_1,'filled');
hold on
scatter(PGA_2,PGV_2,[],FC_2,'s','filled');
hold on
scatter(PGA_3,PGV_3,[],FC_3,'^','filled');
hold on
a = colorbar;
% colormap(flipud(gray));
colormap(cool);
xlabel('PGA (cm/s²)','FontSize',16)
ylabel('PGV (cm/s)','FontSize',16)
ylabel(a,'fc (Hz)','FontSize',16,'Rotation',90);
grid on;
axis tight;
saveas(gcf,['2D_color_Scattered_basin_',titre,'.png'])

createhist(PGA,'PGA (cm/s^2)','r')
createhist(PGV,'PGV (cm/s)','r')
createhist(PGAt,'PGA (cm/s^2)','k')
createhist(PGVt,'PGV (cm/s)','k')
%close all;


