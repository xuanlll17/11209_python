INSERT INTO 台北市youbike (站點名稱, 行政區, 更新時間, 地址, 總車輛數, 可借, 可還) 
VALUES ('YouBike2.0_一壽橋','文山區','2023-11-10 09:53:15','樟新街64號前方',16,6,10)
ON CONFLICT (站點名稱,更新時間) DO NOTHING 
	  
select * from 台北市youbike
where 站點名稱 = 'YouBike2.0_一壽橋'

--搜尋最新時間的資料
select a.* 
from 台北市youbike a join (select distinct 站點名稱,max(更新時間) 更新時間
from 台北市youbike group by 站點名稱) b 
on a.更新時間=b.更新時間 and a.站點名稱=b.站點名稱

SELECT *
FROM 台北市youbike
WHERE (更新時間,站點名稱) IN (
	SELECT MAX(更新時間),站點名稱
	FROM 台北市youbike
	GROUP BY 站點名稱
) 

--搜尋站點
SELECT *
FROM 台北市youbike
WHERE (更新時間,站點名稱) IN (
	SELECT MAX(更新時間),站點名稱
	FROM 台北市youbike
	GROUP BY 站點名稱
) AND 站點名稱 like '%台北%'

--計算id筆數
SELECT COUNT(id) as 筆數
FROM 台北市youbike






/*
drop table taiwan_pm25

select * from taiwan_pm25
where 城市名稱 = '士林'

SELECT 站點名稱, 行政區, MAX(更新時間) AS 更新時間, 地址, 總車輛數, 可借, 可還
FROM 台北市youbike
GROUP BY 站點名稱, 行政區, 地址, 總車輛數, 可借, 可還

SELECT 站點名稱, 更新時間, 行政區, 地址, 總車輛數, 可借, 可還
FROM 台北市youbike
WHERE 更新時間 IN (
	SELECT MAX(更新時間)
	FROM 台北市youbike
	GROUP BY 站點名稱
)
GROUP BY 站點名稱, 行政區, 地址, 總車輛數, 可借, 可還

SELECT DISTINCT ON (站點名稱) 站點名稱, 更新時間, 行政區, 地址, 總車輛數, 可借, 可還
FROM 台北市youbike
ORDER BY 站點名稱, 更新時間 DESC;

INSERT INTO 台北市youbike (站點名稱, 行政區, 更新時間, 地址, 總車輛數, 可借, 可還) 
VALUES ('YouBike2.0_一壽橋','文山區','2023-11-10 09:53:15','樟新街64號前方',1,6,10)
ON CONFLICT (站點名稱,更新時間) DO UPDATE 
  SET 總車輛數 = 16, 
      可借 = 6,
	  可還 = 10;
*/
