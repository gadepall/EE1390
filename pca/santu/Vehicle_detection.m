clc; clear all; close all;

% load the data
load CSI_Vehicle_Backgroung_all.mat;

% rearrange the data %
Y = permute(csi_background_1a,[3 2 1]); csi_background_1a_vector= Y(:,:);Y = permute(csi_vehicle_1a,[3 2 1]); csi_vehicle_1a_vector= Y(:,:);
Y = permute(csi_background_2a,[3 2 1]); csi_background_2a_vector= Y(:,:);Y = permute(csi_vehicle_2a,[3 2 1]); csi_vehicle_2a_vector= Y(:,:);
Y = permute(csi_background_3a,[3 2 1]); csi_background_3a_vector= Y(:,:);Y = permute(csi_vehicle_3a,[3 2 1]); csi_vehicle_3a_vector= Y(:,:);
Y = permute(csi_background_4a,[3 2 1]); csi_background_4a_vector= Y(:,:);Y = permute(csi_vehicle_4a,[3 2 1]); csi_vehicle_4a_vector= Y(:,:);
Y = permute(csi_background_5a,[3 2 1]); csi_background_5a_vector= Y(:,:);Y = permute(csi_vehicle_5a,[3 2 1]); csi_vehicle_5a_vector= Y(:,:);

%% PCA and Scatterplot

%%%PCA for combined dataset
data_all = [csi_vehicle_1a_vector;csi_vehicle_2a_vector;csi_vehicle_3a_vector;csi_vehicle_4a_vector;csi_vehicle_5a_vector;...
  csi_background_1a_vector;csi_background_2a_vector;csi_background_3a_vector;csi_background_4a_vector;csi_background_5a_vector;];

[data_pca, lambda, mapping] = pca_eig_santu(data_all, 50);

% cumulative energy contribution of each eigenvalues
total_eig_energy = 0;
for i=1:length(lambda)
    total_eig_energy = total_eig_energy+lambda(i)*lambda(i);
end
eta = zeros(length(lambda));
for i=1:length(lambda)
    sq_sum = 0;
    for j=1:i
        sq_sum = sq_sum + lambda(j)*lambda(j);
    end
    eta(i) = 100*sq_sum/total_eig_energy;
end

figure;
subplot(211); stem(lambda(1:10)/max(lambda)); grid on; title('Evaluated and Sorted Eigenvalues (only 1st 10 shown)');
xlabel({'Index of Eigenvalues','(According to Descending Order)'});ylabel({'Eigenvalue'})
subplot(212); plot(eta(1:10)); grid on; title('Cumulative Energy Contribution Of The Eigenvalues (%)');
xlabel({'Index of Eigenvalues','(According to Descending Order)'});ylabel({'Cumulative Energy Contribution','(%)'});

% from the above plot, it is evident that, 50 PCs are adequate
%[data_pca_50, lambda, mapping] = pca_eig_santu(data_all, 50);

data_pca_30 = abs(data_pca(:,1:30));
% figure; imagesc(data_pca_50);
data_target = data_pca_30(1:length(data_pca_30(:,1))/2,:);
data_no_target = data_pca_30(length(data_pca_30(:,1))/2+1:length(data_pca_30(:,1)),:);

%scatter(data_target,data_no_target);

%% cluster plot %%
hest_count = 1000;
data_count = 5;
% % 2d plot
figure; % vehicle detection
for set = 1:5
     for i=1:hest_count
        temp = (set-1)*data_count+i;
        if(set==1)    plot(data_target(temp,1),data_target(temp,2),'b.','MarkerSize',7); hold on; end
        if(set==2)    plot(data_target(temp,1),data_target(temp,2),'bo','MarkerSize',7); hold on; end
        if(set==3)    plot(data_target(temp,1),data_target(temp,2),'b+','MarkerSize',7); hold on; end
        if(set==4)    plot(data_target(temp,1),data_target(temp,2),'bx','MarkerSize',7); hold on; end
        if(set==5)    plot(data_target(temp,1),data_target(temp,2),'bs','MarkerSize',7); hold on; end
     end
     %pause(5); 
     for i=1:hest_count
        temp = (set-1)*data_count+i;
        if(set==1)    plot(data_no_target(temp,1),data_no_target(temp,2),'k.','MarkerSize',7); hold on; end
        if(set==2)    plot(data_no_target(temp,1),data_no_target(temp,2),'ko','MarkerSize',7); hold on; end
        if(set==3)    plot(data_no_target(temp,1),data_no_target(temp,2),'k+','MarkerSize',7); hold on; end
        if(set==4)    plot(data_no_target(temp,1),data_no_target(temp,2),'kx','MarkerSize',7); hold on; end
        if(set==5)    plot(data_no_target(temp,1),data_no_target(temp,2),'ks','MarkerSize',7); hold on; end
     end     
     grid on;
%      pause(2); 
end
hold off;title(sprintf('Vehicle Detection using CommSense: vehicle - Blue, Background - Black'));
% 
% 3d plot
figure; % vehicle detection
for set = 1:5
     for i=1:hest_count
        temp = (set-1)*data_count+i;
        if(set==1)    plot3(data_target(temp,1),data_target(temp,2),data_target(temp,3),'b.','MarkerSize',7); hold on; end
        if(set==2)    plot3(data_target(temp,1),data_target(temp,2),data_target(temp,3),'bo','MarkerSize',7); hold on; end
        if(set==3)    plot3(data_target(temp,1),data_target(temp,2),data_target(temp,3),'b+','MarkerSize',7); hold on; end
        if(set==4)    plot3(data_target(temp,1),data_target(temp,2),data_target(temp,3),'bx','MarkerSize',7); hold on; end
        if(set==5)    plot3(data_target(temp,1),data_target(temp,2),data_target(temp,3),'bs','MarkerSize',7); hold on; end
     end
     %pause(5); 
     for i=1:hest_count
        temp = (set-1)*data_count+i;
        if(set==1)    plot3(data_no_target(temp,1),data_no_target(temp,2),data_no_target(temp,3),'k.','MarkerSize',7); hold on; end
        if(set==2)    plot3(data_no_target(temp,1),data_no_target(temp,2),data_no_target(temp,3),'ko','MarkerSize',7); hold on; end
        if(set==3)    plot3(data_no_target(temp,1),data_no_target(temp,2),data_no_target(temp,3),'k+','MarkerSize',7); hold on; end
        if(set==4)    plot3(data_no_target(temp,1),data_no_target(temp,2),data_no_target(temp,3),'kx','MarkerSize',7); hold on; end
        if(set==5)    plot3(data_no_target(temp,1),data_no_target(temp,2),data_no_target(temp,3),'ks','MarkerSize',7); hold on; end
     end     
     grid on;
     %pause(5); 
end
hold off;title(sprintf('Vehicle Detection using CommSense: Vehicle - Blue, Background - Black'));
% 