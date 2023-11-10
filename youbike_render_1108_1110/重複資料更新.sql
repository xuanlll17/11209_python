INSERT INTO 台北市youbike (站點名稱, 行政區, 更新時間, 地址, 總車輛數, 可借, 可還) 
VALUES ('YouBike2.0_一壽橋','文山區','2023-11-10 09:53:15','樟新街64號前方',16,6,10)
ON CONFLICT (站點名稱,更新時間) DO NOTHING 

INSERT INTO 台北市youbike (站點名稱, 行政區, 更新時間, 地址, 總車輛數, 可借, 可還) 
VALUES ('YouBike2.0_一壽橋','文山區','2023-11-10 09:53:15','樟新街64號前方',1,6,10)
ON CONFLICT (站點名稱,更新時間) DO UPDATE 
  SET 總車輛數 = 16, 
      可借 = 6,
	  可還 = 10;

	  
select * from 台北市youbike
where 站點名稱 = 'YouBike2.0_一壽橋'