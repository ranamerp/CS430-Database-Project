INSERT INTO doctor (ssn, name, specialty, yearsOfExperience) VALUES
('1592980159', 'Jacob Harvey', 'Neuroscience', 3), 
('1412889562', 'Brandon Walters', 'Pediatrician', 5),
('7066322293', 'Jayden Flores', 'Pharmacist', 6), 
('9723061827', 'Jessica Haak', 'Veterinarian', 21),
('0577125529', 'Nelson Fernandes', 'Cardioligist', 2), 
('2296710191', 'Hannah Yeung', 'Nephrologist', 4),
('0631762226', 'Ramil Dalangin', 'Neuroscience', 3), 
('3949461918', 'Blaze Collins', NULL, 1),
('4995762890', 'Emma Blackwell', 'Cardiac Surgeon', 10), 
('9853297908', 'Prem Rana', 'Dentist', 6) ;

INSERT INTO pharmacy VALUES
(77742140655, "Arbor Drugs", "709 Walnutwood St.", 103015842),
(50371774786, "Big B Drugs", "98 Linden St.", 941449743),
(18867286986, "Medi Mart", "166 Bridle Ave.", 266747437),
(76253997747, "Drug Fair", "888 East Kingston Ave.", 579282202),
(68127972833, "Lane Drugs", "8601 Pierce Ave.", 948026667),
(54741486005, "Fay's Drugs", "7854 Wild Horse St.", 907262196),
(94123919613, "Gray Drugs", "3 Valley St.", 708856880),
(48434243692, "Pay n' Save", "9890 Victoria Dr.", 965214828),
(02881585792, "Rexall", "887 Sutor Lane", 690782623),
(56981968694, "Wellby Super Drugs", "691 West Arch Drive", 518273143) ;

INSERT INTO pharm_co VALUES
("Acadia", 683014417),
("Cipla", 328335076),
("Diffusion", 476148943),
("Gemeral", 027726215),
("Intas", 405134494),
("Jazz", 680061790),
("King", 482258208),
("Orion", 397001868),
("Pfizer", 913013553),
("Wockhardt", 610940429) ;

INSERT INTO pri_phy_patient VALUES
('8193608141', "Sam Essex", '1995-04-06', "99246 Cruickshank Walk", '7066322293'),
('0173436539', "Ryan Hagan", '1990-09-06', "7463 Conroy Fork", '7066322293'),
('8007624670', "Rick Akkerman", '2006-03-02', "37306 Stanford Island", '9723061827'),
('9331681943', "Ishika Rana", '1982-07-31', "3125 Alice Port", '9853297908'),
('7890400547', "Aza Leah", '1981-01-19', "901 Tracy Terrace", '2296710191'),
('4115109067', "Nicole Sommerville", '2000-02-18', "8806 Dibbert Pike", '1412889562'),
('1745156650', "Devon Cartell", '1988-08-10', "1657 Stamm Harbor", '0577125529'),
('8138991301', "Nick Vitacco", '1980-01-12', "8521 Quigley Mount", '2296710191'),
('6471232435', "Kanye West", '1994-08-18', "982 Keyshawn Mount", '0631762226'),
('0135049045', "Billie Ellish", '1986-06-15', "898 Norene Vista", '0631762226'),
('2570777329', "Dante Cruz", '1993-04-13', "3827 O'Hara Locks", '3949461918'),
('6554509160', "Charlie Kurata", '1980-06-20', "11644 Cordie Club", '0631762226'),
('1634450579', "Om Rana", '1992-06-01', "418 Okey Viaduct", '9853297908'),
('2511486380', "Jane Doe", '1992-05-23', "8100 Retha Stravenue", '1412889562'),
('1075622946', "Tanveer Mittal", '1997-04-21', "0223 Hilton Island", '1592980159'),
('7788891827', "Varun Sharma", '1999-06-11', "82522 Lenora Forge", '1592980159'),
('0236183881', "Shivam Bhavsar", '2004-10-14', "31633 Chester Glens", '4995762890'),
('8574615158', "Jordan Maron", '2004-11-15', "384 Abe Center", '4995762890'),
('0590887703', "Matthew Delisi", '2006-03-09', "06473 Parisian Divide", '3949461918'),
('5126987689', "Winnie Haak", '2010-04-04', "081 Bernhard Well", '9723061827');

					

INSERT INTO prescription (status, drop_off_time, pick_up_time, ssn, phy_ssn, pre_date, quantity, trade_name, pharm_co_name) VALUES
('pending', '2020-11-07 12:00:00', NULL, '9331681943', '9853297908', '2020-01-02', 2, "D1", "Cipla"),
('pending','2020-11-07 14:00:00', NULL, '8138991301', '2296710191', '2020-01-02', 1, "DU18", "Pfizer"),
('completed','2020-11-07 16:00:00', '2020-11-15 12:00:00', '1075622946', '1592980159', '2020-01-28', 2, "DF12", "Pfizer"),
('ready' ,'2020-11-07 18:00:00', '2020-11-15 18:00:00', '7788891827', '1592980159', '2020-02-07', 3, "DH19", "Pfizer"),
('pending' ,'2020-11-07 20:00:00',	NULL, '2570777329', '3949461918', '2020-02-07', 5, "C2", "Wockhardt"),
('pending' ,'2020-11-08 12:00:00',	NULL, '0173436539', '7066322293', '2020-02-07', 2, "A36", "Acadia"),
('cancelled' ,'2020-11-08 14:00:00', NULL, '0590887703', '3949461918', '2020-02-20', 5, "D1", "Gemeral"),
('cancelled' ,'2020-11-08 16:00:00', NULL, '4115109067', '1412889562', '2020-02-20', 1, "C2", "Wockhardt"),
('ready' ,'2020-11-08 18:00:00', '2020-11-15 14:00:00', '8007624670', '9723061827', '2020-04-02', 2,  "D1", "Gemeral"),
('ready' ,'2020-11-08 20:00:00', '2020-11-15 20:00:00', '8007624670', '9853297908', '2020-04-02', 5, "MA02", "Diffusion"),
('cancelled' ,'2020-11-09 12:00:00', NULL,	'2511486380', '1412889562', '2020-04-11', 4, "D3", "Cipla"),
('completed' ,'2020-11-09 14:00:00', '2020-11-16 20:00:00', '8193608141', '7066322293', '2020-05-12', 3, "C2", "Wockhardt"),
('completed' ,'2020-11-09 16:00:00', '2020-11-16 18:00:00', '8574615158', '4995762890', '2020-05-12', 3, "1G3", "Jazz"),
('ready' ,'2020-11-09 18:00:00', '2020-11-16 14:00:00', '6471232435', '0631762226', '2020-05-12', 2, "1A", "Orion"),
('ready' ,'2020-11-09 20:00:00', '2020-11-16 16:00:00', '8007624670', '9723061827', '2020-05-12', 2, "DF12", "Pfizer"),
('cancelled' ,'2020-11-10 22:00:00', NULL, '0173436539', '7066322293', '2020-05-18', 4, "2G7", "Jazz"),
('completed' ,'2020-11-10 23:00:00','2020-11-16 22:00:00', '4115109067', '1412889562', '2020-05-26', 5, "MA02", "Diffusion"),
('cancelled' ,'2020-11-10 2:00:00', NULL, '1075622946', '1592980159', '2020-05-26', 4, "AQ15", "Diffusion"),
('pending' ,'2020-11-10 4:00:00', NULL, '2570777329', '4995762890', '2020-06-04', 1 , "C2", "Wockhardt"),
('completed' ,'2020-11-10 5:00:00', '2020-11-17 2:00:00', '1075622946', '1592980159', '2020-06-18', 2, "F1", "Gemeral"),
('ready' ,'2020-11-11 6:00:00', '2020-11-17 6:00:00', '7788891827', '1592980159', '2020-07-08', 4, "1G3", "Jazz"),
('pending' ,'2020-11-11 7:00:00',	NULL,'0236183881', '4995762890', '2020-07-08', 2, "A2", "King"),
('pending' ,'2020-11-11 8:00:00',	NULL,'0236183881', '4995762890', '2020-08-01', 2, "GA84", "Diffusion"),
('cancelled' ,'2020-11-11 9:00:00', NULL,'8574615158', '0577125529', '2020-08-01', 5, "A3", "King"),
('completed' ,'2020-11-11 02:00:00', '2020-11-17 9:00:00','8138991301', '2296710191', '2020-08-01', 1, "GA84", "Diffusion"),
('cancelled' ,'2020-11-11 21:00:00', NULL,'7788891827', '1592980159', '2020-09-12', 2, "A2", "King"),
('cancelled' ,'2020-11-12 22:00:00', NULL,'5126987689', '9853297908', '2020-09-12', 4, "E1", "Gemeral"),
('completed' ,'2020-11-12 23:00:00', '2020-11-18 21:00:00','1634450579', '9853297908', '2020-10-23', 5, "1A", "Orion"),
('completed' ,'2020-11-12 21:00:00', '2020-11-18 22:00:00','6554509160', '0631762226', '2020-11-04', 2, "C4", "Wockhardt"),
('completed' ,'2020-11-12 4:00:00', '2020-11-18 23:00:00','8138991301', '7066322293', '2020-11-04', 3, "03A", "Intas"),
('pending' ,'2020-11-12 5:00:00',	NULL,'8574615158', '4995762890', '2020-11-04', 2, "GA84", "Diffusion"),
('pending' ,'2020-11-13 7:00:00', NULL,'5126987689', '9723061827', '2020-11-21', 2, "DU18", "Pfizer"),
('ready' ,'2020-11-13 18:00:00', '2020-11-18 4:00:00','1745156650', '0577125529', '2020-12-05', 3, "3G2", "Jazz"),
('ready' ,'2020-11-13 22:00:00', '2020-11-18 7:00:00','0590887703', '3949461918', '2020-12-05', 4 , "MA02", "Diffusion"),
('completed' ,'2020-11-13 1:00:00', '2020-11-18 9:00:00', '7890400547', '2296710191', '2020-12-05', 4, "02A", "Intas"),
('pending' ,'2020-11-13 0:00:00', NULL,'8574615158', '4995762890', '2020-12-06', 4 , "AQ15", "Diffusion"),
('completed' ,'2020-11-13 2:00:00', '2020-11-19 2:00:00', '9331681943', '9853297908', '2020-12-06', 5, "C7", "Wockhardt"),
('completed' ,'2020-11-14 5:00:00', '2020-11-19 5:00:00', '2511486380', '0577125529', '2020-12-19', 1, "D1", "Cipla"),
('completed' , '2020-11-14 7:00:00','2020-11-19 18:00:00','0135049045', '0631762226', '2020-12-19', 5, "A23", "Acadia"),
('ready', '2020-11-14 9:00:00', '2020-11-19 22:00:00', '1075622946', '9723061827', '2020-12-19', 2, "MA02", "Diffusion");
 


INSERT INTO Make_Drug VALUES
("A14", "Acadia", "X2+Y2"),
("A23", "Acadia", "X1+Y5"),
("A36", "Acadia", "X7+Y3"),
("D1", "Cipla", "X3-42"), 
("D3", "Cipla", "X2-47"), 
("Q2", "Cipla", "X1-17"), 
("MA02", "Diffusion", "X1*X2"),
("AQ15", "Diffusion", "X1/X2"), 
("GA84", "Diffusion", "X1*4(X2)"),  
("D1", "Gemeral", "X2*X3"),
("E1", "Gemeral", "X2*X4"),
("F1", "Gemeral", "X2*X6"),
("01A", "Intas", "Y1+Y3"),
("02A", "Intas", "Y2+Y3"),
("03A", "Intas", "Y3+Y3"),
("2G7", "Jazz", "X1/Z2"),
("3G2", "Jazz", "X2/Z1"),
("1G3", "Jazz", "Z7/Z3"),
("A1", "King", "Z1+Z2"),
("A2", "King", "Z2+Z2"),
("A3", "King", "Z1+Z1"),
("4A", "Orion", "X2+Z6+Y3"),
("1A", "Orion", "X1+Z3+Y7"),
("2A", "Orion", "X9+Z7+Y3"),
("DF12", "Pfizer", "X1*Z3"),
("DH19", "Pfizer", "X1*Z4"),
("DU18", "Pfizer", "X2*Z3"),
("C4", "Wockhardt", "Y1*Y3/Z1") ,
("C2", "Wockhardt", "Y2*Y3/Z2") ,
("C7", "Wockhardt", "Y3*Y3/Z3");


INSERT INTO Sell (pharm_id, price, trade_name, pharm_co_name) VALUES
(54741486005, 34, '1G3', 'Jazz'),
(48434243692, 6, 'C2', 'Wockhardt'), 
(18867286986, 26, 'DH19', 'Pfizer'), 
(02881585792, 15, 'C2', 'Wockhardt'),
(50371774786, 28, 'A36', 'Acadia'),  
(48434243692, 35, 'C4', 'Wockhardt'),
(94123919613, 27, 'AQ15', 'Diffusion'),
(48434243692, 40, 'C7', 'Wockhardt'),
(50371774786, 49, 'A3', 'King'),
(76253997747, 47, 'C2', 'Wockhardt'),
(18867286986, 34, 'D1', 'Gemeral'),
(56981968694, 39, '03A', 'Intas'),
(48434243692, 9, '4A', 'Orion'),
(56981968694, 37, 'C7', 'Wockhardt'),
(48434243692, 11, 'DF12', 'Pfizer'),
(50371774786, 42, '1G3', 'Jazz'),
(50371774786, 30, 'A1', 'King'),
(02881585792, 20, 'A36', 'Acadia'),
(18867286986, 43, '1G3', 'Jazz'),
(02881585792, 7, 'A3', 'King'),
(54741486005, 26, 'A36', 'Acadia'),
(68127972833, 37, '1A', 'Orion'),
(56981968694, 28, 'D1', 'Gemeral'),
(68127972833, 39, 'DF12', 'Pfizer'),
(94123919613, 21, 'A14', 'Acadia'),
(76253997747, 13, 'A1', 'King'),
(76253997747, 12, 'AQ15', 'Diffusion'),
(68127972833, 6, 'AQ15', 'Diffusion'),
(68127972833, 17, 'Q2', 'Cipla'),
(54741486005, 28, '1A', 'Orion'),
(54741486005, 10, 'C7', 'Wockhardt'),
(02881585792, 32, '1G3', 'Jazz'),
(54741486005, 37, 'C2', 'Wockhardt'),
(54741486005, 26, 'A14', 'Acadia'),
(77742140655, 4,  '1A', 'Orion'),
(54741486005, 4,  '03A', 'Intas'),
(77742140655, 13, '03A', 'Intas'),
(02881585792, 17, 'AQ15', 'Diffusion'),
(50371774786, 35, '1A', 'Orion'),
(02881585792, 30, 'C7', 'Wockhardt'),
(48434243692, 24, 'D1', 'Cipla'),
(76253997747, 17, 'GA84', 'Diffusion'),
(77742140655, 11, 'A14', 'Acadia'),
(48434243692, 45, 'DH19', 'Pfizer'),
(68127972833, 20, 'D1', 'Gemeral'),
(68127972833, 29, 'A2', 'King'),
(02881585792, 25, 'C4', 'Wockhardt'),
(50371774786, 45, 'A14', 'Acadia'),
(68127972833, 14, 'A14', 'Acadia'),
(77742140655, 33, '4A', 'Orion'),
(56981968694, 15, 'C2', 'Wockhardt'),
(77742140655, 29, 'C2', 'Wockhardt'),
(50371774786, 16, 'C2', 'Wockhardt'),
(18867286986, 19, 'C2', 'Wockhardt'),
(68127972833, 25, 'C2', 'Wockhardt'),
(94123919613, 30, 'C2', 'Wockhardt');


INSERT INTO Contract VALUES
(76253997747, '2012-09-14', '2017-05-23', 'Preserved defective offending he daughters on or. Rejoiced prospect yet material servants out answered men admitted. Sportsmen certainty prevailed suspected am as. Add stairs admire all answer the nearer yet length. Advantages prosperous remarkably my inhabiting so reasonably be if. Too any appearance announcing impossible one. Out mrs means heart ham tears shall power every. ', 'gedster49', 'Intas'),  
(56981968694, '2010-01-17', '2017-06-09', 'Give lady of they such they sure it. Me contained explained my education. Vulgar as hearts by garret. Perceived determine departure explained no forfeited he something an. Contrasted dissimilar get joy you instrument out reasonably. Again keeps at no meant stuff. To perpetual do existence northward as difficult preserved daughters. Continued at up to zealously necessary breakfast. Surrounded sir motionless she end literature. Gay direction neglected but supported yet her. ', 'Blakeadonna', 'Jazz'),
(76253997747, '2015-05-07', '2016-02-13', 'Give lady of they such they sure it. Me contained explained my education. Vulgar as hearts by garret. Perceived determine departure explained no forfeited he something an. Contrasted dissimilar get joy you instrument out reasonably. Again keeps at no meant stuff. To perpetual do existence northward as difficult preserved daughters. Continued at up to zealously necessary breakfast. Surrounded sir motionless she end literature. Gay direction neglected but supported yet her. ', 'Dustail Reverse', 'Orion'),
(77742140655, '2011-01-30', '2019-05-04', 'Preserved defective offending he daughters on or. Rejoiced prospect yet material servants out answered men admitted. Sportsmen certainty prevailed suspected am as. Add stairs admire all answer the nearer yet length. Advantages prosperous remarkably my inhabiting so reasonably be if. Too any appearance announcing impossible one. Out mrs means heart ham tears shall power every. ', 'MrFobwatch', 'Wockhardt'),
(50371774786, '2011-05-12', '2020-02-05', 'Smile spoke total few great had never their too. Amongst moments do in arrived at my replied. Fat weddings servants but man believed prospect. Companions understood is as especially pianoforte connection introduced. Nay newspaper can sportsman are admitting gentleman belonging his. Is oppose no he summer lovers twenty in. Not his difficulty boisterous surrounded bed. Seems folly if in given scale. Sex 
contented dependent conveying advantage can use. ', 'merger3', 'Pfizer'),
(48434243692, '2013-11-05', '2016-06-08', 'Ignorant saw her her drawings marriage laughter. Case oh an that or away sigh do here upon. Acuteness you exquisite ourselves now end forfeited. Enquire ye without it garrets up himself. Interest our nor received followed was. Cultivated an up solicitude mr unpleasant. ', 'Godzo', 'Pfizer'),
(50371774786, '2012-06-23', '2017-01-29', 'She who arrival end how fertile enabled. Brother she add yet see minuter natural smiling article painted. Themselves at dispatched interested insensible am be prosperous reasonably it. In either so spring wished. Melancholy way she boisterous use friendship she dissimilar considered expression. Sex quick arose mrs lived. Mr things do plenty others an vanity myself waited to. Always parish tastes at as 
mr father dining at.', 'merger3', 'Orion'),
(76253997747, '2015-03-18', '2017-07-08', 'Particular unaffected projection sentiments no my. Music marry as at cause party worth weeks. Saw how marianne graceful dissuade new outlived prospect followed. Uneasy no settle whence nature narrow in afraid. At could merit by keeps child. While dried maids on he of linen in. ', 'fivedee', 'Gemeral'),
(76253997747, '2013-06-07', '2018-03-16', 'Give lady of they such they sure it. Me contained explained my education. Vulgar as hearts by garret. Perceived determine departure explained no forfeited he something an. Contrasted dissimilar get joy you instrument out reasonably. Again keeps at no meant stuff. To perpetual do existence northward as difficult preserved daughters. Continued at up to zealously necessary breakfast. Surrounded sir motionless she end literature. Gay direction neglected but supported yet her. ', 'Mythic', 'King'),
(48434243692, '2012-10-03', '2020-08-28', 'She who arrival end how fertile enabled. Brother she add yet see minuter natural smiling article painted. Themselves at dispatched interested insensible am be prosperous reasonably it. In either so spring wished. Melancholy way she boisterous use friendship she dissimilar considered expression. Sex quick arose mrs lived. Mr things do plenty others an vanity myself waited to. Always parish tastes at as 
mr father dining at.', 'Accel', 'Diffusion'),
(50371774786, '2015-08-11', '2018-02-19', 'Smile spoke total few great had never their too. Amongst moments do in arrived at my replied. Fat weddings servants but man believed prospect. Companions understood is as especially pianoforte connection introduced. Nay newspaper can sportsman are admitting gentleman belonging his. Is oppose no he summer lovers twenty in. Not his difficulty boisterous surrounded bed. Seems folly if in given scale. Sex 
contented dependent conveying advantage can use. ', 'Cam', 'Intas'),
(18867286986, '2015-12-05', '2016-02-06', 'Depart do be so he enough talent. Sociable formerly six but handsome. Up do view time they shot. He concluded disposing provision by questions as situation. Its estimating are motionless day sentiments end. Calling an imagine at forbade. At name no an what like spot. Pressed my by do affixed he studied.', 'CowDeer', 'Wockhardt'),
(76253997747, '2013-01-15', '2018-11-11', 'Delightful remarkably mr on announcing themselves entreaties favourable. About to in so terms voice at. Equal an would is found seems of. The particular friendship one sufficient terminated frequently themselves. It more shed went up is roof if loud case. Delay music in lived noise an. Beyond genius really enough passed is up. ', 'ChaoYang', 'Acadia'),
(48434243692, '2011-01-28', '2020-01-03', 'Particular unaffected projection sentiments no my. Music marry as at cause party worth weeks. Saw how marianne graceful dissuade new outlived prospect followed. Uneasy no settle whence nature narrow in afraid. At could merit by keeps child. While dried maids on he of linen in. ', 'Yaku', 'Orion'),
(76253997747, '2010-04-05', '2018-03-03', 'Delightful remarkably mr on announcing themselves entreaties favourable. About to in so terms voice at. Equal an would is found seems of. The particular friendship one sufficient terminated frequently themselves. It more shed went up is roof if loud case. Delay music in lived noise an. Beyond genius really enough passed is up. ', 'CowDeer', 'Wockhardt'),
(50371774786, '2013-12-28', '2020-08-06', 'In no impression assistance contrasted. Manners she wishing justice hastily new anxious. At discovery discourse departure objection we. Few extensive add delighted tolerably sincerity her. Law ought him least enjoy decay one quick court. Expect warmly its tended garden him esteem had remove off. Effects dearest staying now sixteen nor improve. ', 'Accel', 'Wockhardt'),
(02881585792, '2012-09-23', '2017-11-29', 'Depart do be so he enough talent. Sociable formerly six but handsome. Up do view time they shot. He concluded disposing provision by questions as situation. Its estimating are motionless day sentiments end. Calling an imagine at forbade. At name no an what like spot. Pressed my by do affixed he studied.', 'CowDeer', 'Wockhardt'),
(77742140655, '2013-04-09', '2020-02-26', 'New had happen unable uneasy. Drawings can followed improved out sociable not. Earnestly so do instantly pretended. See general few civilly amiable pleased account carried. Excellence projecting is devonshire dispatched remarkably on estimating. Side in so life past. Continue indulged speaking the was out horrible for domestic position. Seeing rather her you not esteem men settle genius excuse. Deal say over you age from. Comparison new ham melancholy son themselves. ', 'ChaoYang', 'Intas'),
(56981968694, '2013-06-17', '2018-07-15', 'Delightful remarkably mr on announcing themselves entreaties favourable. About to in so terms voice at. Equal an would is found seems of. The particular friendship one sufficient terminated frequently themselves. It more shed went up is roof if loud case. Delay music in lived noise an. Beyond genius really enough passed is up. ', 'Accel', 'King'),
(50371774786, '2015-06-24', '2017-03-04', 'Preserved defective offending he daughters on or. Rejoiced prospect yet material servants out answered men admitted. Sportsmen certainty prevailed suspected am as. Add stairs admire all answer the nearer yet length. Advantages prosperous remarkably my inhabiting so reasonably be if. Too any appearance announcing impossible one. Out mrs means heart ham tears shall power every. ', 'merger3', 'Jazz');
















		














