# DECISION TREE ve RANDOM FOREST KULLANARAK DİYABET HASTALIKLARI VERİ ANALİZİ ve SINIFLANDIRILMASI

# Makine Öğrenmesi Nedir?

Makine öğrenmesi, yapay zekanın bir alt dalıdır. Sistemlerin verilere dayanarak öğrenmesini ve performansını iyileştirmesini hedefler. Makine öğrenmesi, bilgisayarları programlamak yerine onları deneyim sahibi yaparak deneyimlerle geliştirilmesini amaçlamaktadır. Başka bir örnekle makine öğrenmesi, büyük veri setlerinde desenleri ve ilişkileri bulmak için algoritmalar kullanılması örnek gösterilebilir. Bu algoritmalar veri analizinde en iyi kararları veya tahminleri yapmak için eğitilir. Örnek olarak bu araştırmanın konusu olan diyabet hastalıklarına dair bir makine öğrenmesi algoritmaları kullanılarak analiz söylenebilmektedir. Makine öğrenmesi günümüzde birçok alanda kullanım alanına sahiptir. Bu alanlar: Akıllı ev sistemleri, alışveriş sistemleri, eğlence sektörleri ve sağlık alanları örnek gösterilebilir.  

# Decision Tree Algoritması Nedir?

Karar ağacı (Decision Tree), veri madenciliği ve makine öğrenmesinde sıklıkla kullanılan bir algoritmadır. Karar ağacı, bir hedef değişkenin değerini, birkaç girdi değişkenine dayanarak tahmin etmek için kullanılan bir model oluşturur. Bu modellemeler üzerinden ise analiz imkanı sunarak veri seti hakkında bizlere fikir verebilmektedir.

Karar ağacı, adından da anlaşılacağı üzere bir ağaç yapısıyla temsil edilir. Her iç düğüm, bir karar noktasını temsil eder ve bir girdi değişkeninin değerine göre dallanır. Her yaprak düğümü ise bir hedef değişkenin tahmin edilen değerini temsil eder. Karar ağacı, veri kümesindeki desenleri ve ilişkileri keşfetmek için girdi değişkenlerini kullanır ve bu bilgiye dayanarak tahminler yapar.

Bu ağaç yapısının temsili görseli Şekil-1’de verilmiştir.

![Şekil-1 Karar Ağacı temsili görseli](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/ml_analiz_1.jpg)

Şekil-1 Karar Ağacı temsili görseli

Karar ağacı algoritmasının standart bir yöntemi yoktur. Birden fazla yöntemi vardır. Birkaç farklı yöntem üzerinden karar ağaçları kullanılabilmektedir.

Karar ağacı algoritmaları arasında popüler olan bazı yöntemler şunlardır:

- ID3 (Iterative Dichotomiser 3): Entropi ve Bilgi Kazanımı (Information Gain) kavramlarına dayanır. Entropi, rastgelelik, belirsizlik ve beklenmeyen durumun ortaya çıkma olasılığını gösterir. Bir veri setinin entropisi, veri örneklerinin tamamen düzenli/homojen olduğu durumda sıfır olurken, değerler birbirine eşit olduğunda entropi 1 olur. Bilgi kazanımı ise bir veri setini bir özellik üzerinde böldükten sonra elde edilen entropi azaltmasına dayanır.
- C4.5: veri setindeki özelliklerin bilgi kazanımını maksimize etmek için en iyi bölme noktalarını seçer. Bilgi kazanımı, bir özelliğin veri setini ne kadar iyi böleceğini ölçer. C4.5 algoritması, veri setindeki özelliklerin kategorik veya sürekli olmasına bakılmaksızın kullanılabilir.
- CART (Classification and Regression Trees): veri setindeki özelliklerin kategorik veya sürekli olmasına bakılmaksızın kullanılabilir. Algoritma, her bir özelliği kullanarak en iyi bölme noktalarını seçer ve bu şekilde veri setini daha homojen alt kümelerine böler. Sınıflandırma problemlerinde, her bir yaprak düğümü bir sınıfı temsil ederken, regresyon problemlerinde yaprak düğümleri sayısal tahmin değerlerini temsil eder.
- Random Forests (Rastgele Ormanlar)
- Gradient Boosting (Gradyan Artırma): bir hedef değişkeni tahmin etmek için bir dizi zayıf öğreniciyi bir araya getirir. Her bir zayıf öğrenici, önceki öğrenicinin hatalarını düzeltmek için eğitilir. Bu şekilde, her bir öğrenici, önceki öğrenicinin hatalarını azaltarak toplam hatayı azaltmaya çalışır.

Karar ağaçları, sınıflandırma ve regresyon gibi birçok problemin çözümüne uyarlanabilir. Sınıflandırma problemlerinde, bir karar ağacı, bir veri örneğini belirli bir sınıfa atamak veya uyarlamak için kullanılabilir. Regresyon problemlerinde ise, bir karar ağacı, bir hedef değişkenin sayısal değerini tahmin etmek için kullanılabilir.

Karar ağaçları ayrıca, veri madenciliği ve keşif analizi gibi alanlarda da yaygın olarak kullanılır. Karar ağaçları, veri setindeki önemli değişkenleri belirlemek, veri setini sınıflandırmak veya özellikleri tahmin etmek için kullanılabilir.

# Random Forest Nedir?

Random Forest, (Rastgele Orman) algoritması sınıflandırma ve regresyon problemleri için kullanılan bir makine öğrenimi algoritmasıdır. Random Forest, birden çok karar ağacını bir araya getirerek bir topluluk oluşturur.

Random Forest algoritması, her bir karar ağacını farklı bir gözlem örneği üzerinde eğiterek çeşitli modeller oluşturur. Bu modeller, sınıflandırma veya regresyon problemlerinde kullanılarak tahminler yapar. Her bir karar ağacı, veri setindeki desenleri ve ilişkileri temsil eder.

Şekil-2’de örnek bir Random Forest görseli verilmiştir.

![Şekil-2 Random Forest Modeli](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/ml_analiz_2.jpg)

Şekil-2 Random Forest Modeli

Random Forest algoritması, her bir karar ağacının bağımsız olarak çalışmasını sağlar ve her bir ağacın tahminlerini birleştirerek son bir tahmin yapar. Bu, daha iyi bir genelleme yeteneği sağlar.

Random Forest algoritması, veri setindeki önemli özellikleri belirlemek için de kullanılabilir. Her bir ağaç, veri setini farklı özelliklerle eğitir ve bu sayede hangi özelliklerin daha önemli olduğunu belirlemek için bir ölçüt sağlar.

Random Forest algoritması, genellikle yüksek boyutlu ve karmaşık veri setlerinde iyi performans gösterir. Ayrıca, eksik verilerle başa çıkabilme yeteneği ve aşırı uyum (overfitting) riskini azaltma özelliği gibi avantajlara sahiptir.

### DİYABET TANIMI

Diyabet veya halk arasında bilinen adıyla şeker hastalığı, genel anlamda kanda bulunan glukoz (şeker) seviyesinin normalin üzerinde çıkması durumudur. Bu durum vücudun şeker dengesini sağlamakla görevli olan pankreasın yeterli miktarda insülin hormonu üretememesi veya bu hormonu kullanamamasından kaynaklanmaktadır. Diyabetin iki farklı çeşidi vardır. Tip-1 diyabette pankreasın insülin yeteneğini tamamen kaybetmiş olduğu genetik bir hastalıktır. Tip-2 diyabet ise vücudun insülini etkili bir şekilde kullanamadığı veya yeterli miktarda üretemediği bir durumdur. Bunlardan ayrı olarak kadınlarda sadece hamilelik döneminde ortaya çıkan gestasyonel diyabet adı verilen bir diyabet türü daha vardır. Bu diyabet türü geçici bir duruma sahip olduğundan bahsedebiliriz. 

 Uluslararası Diyabet Federasyonu (IDF) verilerine göre IDF diyabet atlasının 2019 tahminlerine göre Dünyada her 11 kişiden birinin diyabetli olduğunu, ülkemizde ise 20-79 yaş arasında bulunan bireyler arasında toplamda 7 milyon kişinin diyabet hastalığına sahip olduğu söylenmektedir. Bu 7 milyon kişinin toplam genç nüfusa oranı yaklaşık olarak %15’ine denk geldiği söylenebilmektedir.

Son olarak şeker hastalığı genel anlamda düzenli olarak takip edilmesi ve uygun tedavi yöntemleriyle kontrol altına alınması gereken bir hastalık olduğundan bahsedebiliriz.

# VERİ SETİMİZİN ÖZELLİKLERİ

Kaggle üzerinden elde ettiğimiz diyabet veri setinde 768 satır ve 9 tane sütun bulunmaktadır. Bu sütunlar sırasıyla;

- Pregnancies: Bir kadının hamile kalma sayısı
- Glucose: Ağız yoluyla elde edilen 2 saatlik plazma glikoz konsantrasyonu
- BloodPressure: Diyastolik kan basıncı (mm-hg)
- SkinThickness: Triceps cilt kıvrım kalınlığı (mm)
- Insulin: 2 saatlik serum insülini (mu U / ml)
- BMI: Vücut Kitle İndeksi ((ağırlık (kg) / boy (boy))^2)
- Age: Yaş
- DiabetesPedigreeFunction: aile geçmişine dayalı olarak diyabet olasılığı fonksiyonu (genetik yatkınlık)
- Outcome: Sonuç durumu (sonuç eğer 0’sa diyabet değildir.) (sonuç eğer 1’se diyabetlidir.)

Veri setimiz içerisinde modelleme yapmadan önce farklı istatistiksel sonuçlara ulaşmak farklı yöntemlere başvurulabilir. Bu yüzden dolayı bu verilerin bize belirli bir anlam sağlayacağı ve verilerimizi daha iyi anlayabileceğimiz düşüncesiyle Numpy kütüphanesinde bulunan *describe (include= “all”)* methodunu kullandık ve istatistiksel sonuçlar ise Şekil-3’de verilmiştir.

![Şekil-3 Veri seti hakkında genel istatiksel bilgiler](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/Ekran_grnts_2023-12-25_174132.png)

Şekil-3 Veri seti hakkında genel istatiksel bilgiler

Şekil-3’de yer alan çıktı kullanmış olduğumuz veri setinin çerçevesinin istatiksel özetini göstermektedir. İstatistikler her bir sütun için ayrı bir hesaplandığını gösterir. Çıktımızı ise şu şekilde yorumlayabiliriz:

- ***“count”:*** Her bir sütundaki veri noktalarının sayısını yani toplam veri adetini gösterir. Bu duruma göre her bir sütunda toplamda 768 adet veri olduğunu söyleyebiliriz.
- ***“mean”:*** Her bir sütundaki veri noktalarının ortalamasını gösterir. Örneğin *“Glucose”* sütununda ortalama glikoz seviyesi 120.89’tur.
- ***“std”:*** Her bir sütundaki veri noktalarının standart sapmasını gösterir. Standart sapma, veri noktalarının ne kadar yayıldığını gösterir. Örneğin *“Glucose”* sütununun standart sapması 31.97’tir.
- ***“min”:*** her bir sütundaki en düşük değeri gösterir.
- ***“25%”:*** Her bir sütundaki değerlerin %25’ini gösterir. Bu değer, veri noktalarının alt çeyreğini temsil eder.
- ***“50%”:*** Her bir sütundaki değerlerin %50’ini gösterir. Bu değer, veri noktalarının medyanını temsil etmektedir.
- ***“75%”:*** Her bir sütundaki değerlerin %75’ini gösterir. Bu değer, veri noktalarının üst çeyreğini temsil etmektedir.
- ***“max”:*** Her bir sütundaki en büyük değeri gösterir.

Bu değerlerin hepsi bizlere veri seti üzerinde değişkenlerin dağılımı, merkezi eğilim ölçüleri gibi temel istatistik bilgiler sunmaktadır.

Sütunlar hakkında ayrıntılı bilgiler ise Şekil-4’de verilmiştir.

![Şekil-4 Sütunlar hakkında ayrıntılı bilgiler.](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/Ekran_grnts_2023-12-25_180532.png)

Şekil-4 Sütunlar hakkında ayrıntılı bilgiler.

Bu şekilde veri atlaması (null) değerinin olup olmadığını, verilerin adet sayısını, verilerin hangi tipte olduğunu kontrol etmiş olduk.

İstatistiksel yöntemler sayısal verilerde bazen bizlere verileri anlama konusunda çok yardımcı olmayabilir. Bundan dolayı ise bu sayısal verileri bir grafik haline getirmekte fayda vardır. Bu grafikler sütunlarda bulunan sayısal değerlerin ortalama dağılımları ve aykırı (outlier) değerler hakkında bir bilgi verebilir. Bu çizimler, Google’ın süper bilgisayar tabanlı kod editörü *COLAB* üzerinden *plot* kullanarak çizilmiştir.

Şekil-5’te *“Pregnancies”* yani hamilelik sayısı ile *“Glucose”* glikoz sayısının ortalama dağılımı gösterilmiştir.

![Şekil-5 Pregnancies ve Glucose veri sütunlarındaki sayısal dağılımı](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/indir.png)

Şekil-5 Pregnancies ve Glucose veri sütunlarındaki sayısal dağılımı

*“Pregnancies”* ve *“Glucose”* grafikleri, farklı değerlere sahip doğum sayıları ve glikoz seviyelerinin maksimum ve minimum sayılarını verir.

Şekil-6’da *“BloodPressure”* yani kan basıncı ile *“SkinThickness”* cilt kalınlığının ortalama dağılımı gösterilmiştir.

![Şekil-6 BloodPressure ve SkinThickness veri sütunlarındaki sayısal dağılım](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/indir_(1).png)

Şekil-6 BloodPressure ve SkinThickness veri sütunlarındaki sayısal dağılım

*“BloodPressure”* ve *“SkinThickness”* grafikleri, farklı değerlere sahip kan basınçları ve cilt kalınlıklarını maksimum ve minimum değerlerinin dağılımını vermektedir. *“SkinThickness”* grafiğinde aykırı değer olarak kabul edilen 0 değeri fazla olduğu için grafik sağa doğru şekillenmiştir.

Şekil-7’de *“Insulin”* ile *“BMI”* yani vücut kitle indeksinin ortalama dağılımı gösterilmiştir.

![Şekil-7 Insulin ve BMI veri sütunlarındaki sayısal dağılımı](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/indir_(2).png)

Şekil-7 Insulin ve BMI veri sütunlarındaki sayısal dağılımı

*“Insulin”* ve *“BMI”* grafikleri, farklı değerlere sahip insülin seviyelerini ve vücut kitle indekslerinin maksimum ve minimum değerlerinin dağılımını vermektedir. “Insulin” grafiğinde aykırı değer olarak kabul edilen 0 değeri fazla olduğu için grafik sağa doğru yatkınlık göstermiştir.

Şekil-8’de *“DiabetesPedigreeFunction”* yani genetik yatkınlık olasılık puanIyla ile *“Age”* yani yaşların ortalama dağılımı gösterilmiştir.

![Şekil-8 DiabetesPedigreeFunction ve Age veri sütunlarındaki sayısal dağılımı](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/indir_(3).png)

Şekil-8 DiabetesPedigreeFunction ve Age veri sütunlarındaki sayısal dağılımı

### HİSTOGRAM GRAFİKLERİ

Histogram, istatistiksel verilerin gruplar halinde sıralanarak dağılımını gösteren bir grafik türüdür. Tipik bir histogram grafiği; bir X ekseni, bir Y ekseni ve dikdörtgen sütunlardan oluşur. X ekseni, verilerin belirli aralıklarla gruplandırıldığı aralıkları temsil ederken, Y ekseni bu aralıklardaki değerlerin frekanslarını temsil etmektedir.

Histogramlar; veri bilimi, veri analizi, görüntü işleme, istatistiksel analiz gibi farklı farklı işlemlerde oldukça fazla kullanılır. Genel anlamda karmaşık veri setlerini görselleştirerek bu verileri daha anlamlı hale getiren bir grafik türü olduğundan bahsedebiliriz. Bu şekilde karmaşık verileri daha hızlı bir şekilde özetlemek mümkündür.

Temizlenmemiş ***Diabetes*** veri setinde her bir sütun için yapılan histogram grafikleri Şekil-9’da gösterilmiştir.

![Şekil-9 Temizlenmemiş Diabetes veri seti histogram grafikleri.](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/indir_(4).png)

Şekil-9 Temizlenmemiş Diabetes veri seti histogram grafikleri.

Daha temizlenmemiş veri setinde toplamda 9 adet sütunun histogram grafiklerine yer verilmiştir. Bu grafiklerde daha henüz bir temizleme işlemi gerçekleşmediğinden bu histogram grafikleri modelleme üzerinden yanıltıcı olabilir ama yine de bize veri seti hakkında şu bilgileri verebilmektedir:

- ***“pregnancies”*** yani gebelik için toplamda 768 adet veri olduğundan bahsetmiştik. Bu verilerin dağılımı göz önüne alındığında grafiğin doğrusal-eğimli bir şekilde olduğundan bahsedebiliriz. Bu eğim verilerin doğrusal anlamda dağıldığını gösterir. Ayrıca, x ekseninde bulunan 0.0-2.5 değerleri yani hiç doğum yapmamış ve ortalama 3 doğum yapmış kadınların veri seti içerisinde toplamda 100 ile 140 arasında veri olduğunu yine aynı şekilde veri seti içerisinde verilerin bu aralıkta yoğunlaştığından bahsedebiliriz.
- ***“glucose”*** yani glikoz, veri seti içerisinde doğrusal olarak dağılım gösterdiği söylenemez. Genel anlamda veri setindeki verilerin yoğunlaştığı bölge 75 ile 150 arasında kan şekeri oranında olduğundan bahsedebiliriz. Ayrıca dağılım dışında kalan 0 değerine baktığımızda ise ***“glicose”*** sütununda outlier *(aykırı)* verilerin fazla olduğundan veya diyabet tip-1 rahatsızlığı bulunan hastaların veri seti içerisinde bulunduğundan bahsedebiliriz.
- ***“bloodpresure”*** yani kan basıncı verilerinin 50 ile 100 arasında yoğunlaşmaların olduğunu ayrıca grafik dağılımı dışında gözüken değerlerin ise bu veri sütununda oldukça fazla outlier *(aykırı)* verilerin olduğundan bahsedebiliriz.
- ***“SkinThickness”*** yani cilt kalınlığı, veri setinin içerisinde cilt kalınlığı 0 olan bireyler, diğer cilt kalınlığı seviyelerine göre oldukça baskındır. Cilt kalınlığı 0 olan veriler haricinde 20 mm ile 40 mm arasında ise dağılımın oldukça birbirine benzer verilerden oluştuğunu söyleyebiliriz. (Ayrıca cilt kalınlığının 0 olması pek muhtemel değildir. Bu yüzden bu veriler ilerleyen aşamalarda outlier *(aykırı)* veri olarak tespit edilip, veri setinden arındırılacaktır.)
- ***“insulin”*** ise insülin seviyesi 0 olan kişilerin veri setinin yaklaşık olarak %50’sine hakim olduğundan bahsedebiliriz. Bunun dışında ise *“SkinThickness”* dağılımıyla benzerlik gösterdiğinden bahsedebiliriz. (*”SkinThickness”* veri sütununda olduğu gibi burada da insülin değerinin 0 olması biyolojik açıdan pek mümkün değildir. Bundan ötürü ilerleyen aşamalarda bu veriler outlier *(aykırı)* veri olarak tespit edilip, veri setinden arındırılacaktır.)
- ***“BMI”*** yani Vücut Kitle İndeksi, veri seti içerisinde 20 ile 50 arasında BMI sahip olan insanların bu veri setinde oldukça fazla yoğunlaştığı yorumunu yapabiliriz.
- ***“DiabetesPedigreeFunction”*** yani diyabete genetik yatkınlık fonksiyonunda veri seti içerisinde bilgileri bulunan insanların çoğunluğunun ailesinde 0 veya 1 tane şeker hastası olduğundan bahsedebiliriz.
- ***“Age”*** veri seti içerisinde bulunan insanların yaşları ortalama olarak 20 ile 40 arasında yoğunluk olduğundan bahsedebiliriz. Ayrıca yaşı 20 olan hastaların, veri setinde toplamda 130’a yakın bilgisi olduğunu bahsedebiliriz.
- ***“Outcome”*** yani çıktımız, yukarıda bahsettiğimiz gibi “0” şeker hastalığı teşhisi koyulmamış verileri temsil ederken, “1” ise şeker hastalığı teşhisi koyulmuş insanları belirtir. Bundan ötürü bu veri setinde 500’e yakın kişinin şeker hastası olmadığını yani sağlıklı olduğunu, geri kalanların ise şeker hastası teşhisi koyulmuş olduğunu göstermektedir. Bu bilgiler doğrultusunda veri setinde şeker hastalığı teşhisi koyulmamış veya potansiyel şeker hastası olabilecek hastaların verilerinin fazla olduğundan bahsedebiliriz.

### KORELASYON HARİTASI

Korelasyon, istatistik ve olasılık kuramı alanlarında kullanılan bir yöntemdir. İki veya daha fazla rassal değişken arasındaki doğrusal ilişkinin yönünü ve gücünü belirtmek için kullanılır. Korelasyonlar, veriler arasındaki matıksal ilişkileri anlamak için kullanılır. İstatistik, makine öğrenmesi, finans alanında oldukça fazla başvurulan bir kavramdır.

Korelasyon katsayısı -1 ile +1 arasında bir değer almaktadır. 0 değeri, değişkenler arasında korelasyon olmadığını ifade etmektedir. Değer -1’e yaklaşıyorsa negatif mükemmel korelasyonu, +1’e yaklaşıyorsa ise pozitif mükemmel korelasyonu ifade etmektedir. Bu değerlerin aralıkları ise pozitif veya negatif düşük korelasyon, pozitif veya negatif yüksek korelasyon olarak adlandırılmaktadır. Korelasyon katsayısı, değişkenler arasındaki ilişkinin gücü ve yönü hakkında bilgi vermektedir.

Şekil-10’da Temizlenmemiş *Diabetes* veri setinin korelasyon ısı haritası verilmiştir.

![Şekil-10 Korelasyon ısı haritası](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/indir_(5).png)

Şekil-10 Korelasyon ısı haritası

Şekil-10’da görüntülenen ısı haritasında, daha parlak renkler daha büyük korelasyonu ifade etmektedir. Sadece ısı haritalarına bakarak glikoz seviyelerinin *(Glucose),* yaşın *(Age)*, BMI *(Vücut Kitle İndeksi)* ve gebelik *(Pregnancies)* sayılarının sonuç değişkeni ile  önemli korelasyonlar gösterdiği sonucunu çıkarabiliriz. Tüm özelliklerden yola  çıkarak, veri temizlemesi daha yapılmamış olan veri setinde sonucun *(outcome)* en iyi yordayıcısı glikoz ***(Glucose)*** seviyesidir. 

En iyi yordayıcı sıralaması ise Şekil-11’de verilmiştir.

![Şekil-11 Korelasyon analizi sıralaması](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/Ekran_grnts_2023-12-26_205115.png)

Şekil-11 Korelasyon analizi sıralaması

Bu görsel göz önüne alındığında sonuç *(outcome)* dışında, sonuçla *(outcome)* ile alınmış en iyi korelasyon puanları sırasıyla *0.29* ile *BMI*, *0.23* *Age* olarak olarak sıralanmaktadır.

### TEMİZLENMEMİŞ VERİLERİN DAĞILIM MATRİSİ

Şekil-12’de temizlenmemiş verilerin dağılım matrisi verilmiştir.

![Şekil-12 Temizlenmemiş Diabetes veri setinin matris dağılımları](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/indir_(6).png)

Şekil-12 Temizlenmemiş Diabetes veri setinin matris dağılımları

Bir canlıda glikozun, insülinin, cilt kalınlığının, hayati öneme sahip kan basıncının ve vücut kitlesi indeksi *(BMI)*’nın sıfır olması imkansızdır. Veri seti içerisinde sıfıra sahip olan değerleri ya yerine uygun olarak veri ekleyerek ya da bu alanları boş bırakarak iki yöntemle veri setimizden arındırmamız gerekiyor. Aksi halde hem kuracağımız modellerin çözüm yüzdeleri hatalı sonuçlar verecektir.

Ortalama, ve orijinal veriler çarpık halde olmadığı zamanlarda oldukça kullanışlıdır, medyan ise daha sağlamdır ama aykırı değerlere duyarlı değildir bundan dolayı ise veriler çarpık olduğunda ortalama tercih edilmektedir.

Veri dağılım tabloları göz önüne alındığında insülin *(insulin)*, glikoz *(Glucose)* ve cilt kalınlığı *(SkinThickness)* sağ ve sola serpilmiş bir şekilde dağılmıştır. Bundan dolayı ise bu verilerde sıfır olan değerlerini medyan kullanarak doldurma yaptık. Öte yandan vücut kitle indeksi *(BMI)* ve Kan Basıncını *(BloodPressure)* normal bir dağılıma sahip olduğundan ötürü sıfır olan değerlerini ortalamayı kullanarak doldurma işlemi gerçekleştirdik. 

Veri setimiz üzerindeki değişiklikleri bir for döngüsü içerisinde ***numpy*** kütüphanesinde bulunan ***np.median*** ve ***np.mean*** methodlarını kullanarak gerçekleştirdik.

Şekil-13’de temizlenmiş olan *diabetes* verilerinin histogram grafikleri verilmiştir.

![Şekil-13 temizlenmiş diabetes verilerinde histogram grafiği](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/indir_(7).png)

Şekil-13 temizlenmiş diabetes verilerinde histogram grafiği

Temizlenmemiş verilerle oluşturduğumuz histogram grafiğiyle (Şekil-9), temizlenmiş histogram grafiğini (Şekil-13) kıyaslandığında verilerin daha dengeli bir dağılım gösterdiğini, veri setimizin aykırı veri setlerinden arındığı gözle görünür bir şekilde gerçekleşmiştir.

*Diabetes* veri setini birtakım analizlerden ve temizleme işlemlerinden geçirdikten sonra bu araştırmanın asıl konularından biri olan *Decision Tree* ***(Karar Ağacı)*** kullanarak analiz yapma işlemine geçebiliriz.

## DECISION TREE (KARAR AĞACI) KULLANARAK SINIFLANDIRMA ANALİZİ

*Diabetes* veri setini eğitmeden önce yapılacakları planlamamızda fayda vardır. Denetimli bir makine öğrenimi algoritması olan karar ağacının daha düzgün bir model kurabilmemiz amacıyla temizlenmiş olan veri setini belirli bir parametreye bölerek ve karar düğümleri kullanarak bir sınıflandırma modeli kurgulamamız gerekmektedir.

1. **Özellik Seçimi**: Kod, *"Glucose"*, *"BloodPressure", "SkinThickness", "BMI", "DiabetesPedigreeFunction"* ve *"Age"* sütunlarını içeren *diabets_df3* veri çerçevesinden yeni bir X veri çerçevesi oluşturduk. *“Outcome”* ifadesi sonuç ifadesi olduğu için onu ise sonraki aşamalarda Y veri çerçevesine aktaracağız.
2. **Verinin Bölünmesi**: Denetimli makine öğrenmesi algoritmalarında veriler eğitim ve test olarak ikiye bölünmesi gerekmektedir. Bu bir zorunluluktur. Karar ağacı ise denetimli bir makine öğrenmesi algoritması olması vesilesiyle, *“train_test_split”* fonksiyonu kullanılarak eğitim ve test setlerine bölünmesi gerekir. Veri setimizin büyük olması nedeniyle ve birçok deneme sonucunda ise Test boyutunu %30 olarak belirlenmesi en efektif sonucu vermektedir. Bundan ötürü de Test boyutunu %30 olarak belirledik ve rastgele durumu 1 olarak ayarladık.
3. **Model Eğitimi**: Karar Ağacı sınıflandırıcısı *(DecisionTreeClassifier)* oluşturuldu ve eğitim verileri *(X_train ve Y_train)* ile eğitildi. *“DecisionTreeClassifier”* sınıflandırıcısı *Pyhton’un SKLearn* kütüphanesinde yüklü olan bir methodtur.
4. **Tahmin Yapma**: Eğitilmiş model *(clf)*, test verileri *(X_test)* için tahminde bulunur ve sonuçlar *“y_pred”* değişkeninde saklanır.
5. **Model Değerlendirmesi**: Gerçek değerlerle *(Y_test)* tahmin edilen değerler *(y_pred)* karşılaştırılarak modelin doğruluğu hesaplanır.

Hesaplama sonucu olarak ***%77*** oranında bir sınıflandırma başarı oranı elde ettik. Bunu bir örnekle anlatmak gerekirse veri seti içerisinde bulunan her 100 veri için modelimiz 77 tanesini doğru olarak sınıflandırmıştır.

# DECİSİON TREE ANALİZ SONUCU

### CONFUSION MATRIX

Confusion Matrix (Karmaşıklık Matrisi), bir sınıflandırma modelinin performansını değerlendirmek amacıyla kullanılan bir görselleştirme aracıdır. Confusion Matrix, sınıflandırma modellerinde performansın yorumlanmasına yardımcı olmaktadır ayrıca farklı metrik değerleri bulmamıza ve modelin başarısını ayrıntılı bir şekilde değerlendirmemize olanak sağlar.

Confusion Matrix, sınıflandırma modellerinin tahminlerini gerçek değerlerle karşılaştırarak oluşturur. Bu matrix, dört farklı sonucu içerir. Bunlar:

- **TP (True Positive):** Modelin doğru bir şekilde pozitif olarak tahmin ettiği durum sayısı olarak nitelendirilir.
- **FN (False Negative):** Modelin yanlış bir şekilde negatif olarak tahmin ettiği durum sayısıdır.
- **FP (False Positive):** Modelin yanlış bir şekilde pozitif olarak tahmin ettiği durum sayısıdır.
- **TN (True Negative):** Modelin doğru bir şekilde negatif olarak tahmin ettiği durum sayısıdır.

Confusion Matrix’in bir avantajı ise, kurulmuş olan sınıflandırma modelinin doğruluk *(accuracy)*, hassasiyet *(precision)*, duyarlılık *(recall)* gibi metrikleri de içerisinden elde etmek mümkündür.

Şekil-14’de Diabetes veri setinin Confusion Matrix’i verilmiştir.

![Şekil-14 Diabetes veri setinin karmaşıklık matrisi](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/indir_(9).png)

Şekil-14 Diabetes veri setinin karmaşıklık matrisi

İki farklı sınıf (eğitim ve test) verileri göz önüne alındığında bu görsel şu şekilde yorumlanabilmektedir:

- **Doğru Pozitif (True Positive):** Kurulmuş olan karar ağacı modelin doğru bir şekilde pozitif olarak tahmin ettiği durum sayısı 437’dir.
- **Yanlış Pozitif (False Positive):** Kurulmuş olan karar ağacı modelinin yanlış bir şekilde pozitif olarak tahmin ettiği durum sayısı 63’tür.
- **Yanlış Negatif (False Negative):** Kurulmuş olan karar ağacı modelinin yanlış bir şekilde negatif olarak tahmin ettiği durum sayısı 120’dir.
- **Doğru Negatif (True Negative):** Kurulmuş olan karar ağacı modelinin doğru bir şekilde negatif olarak tahmin ettiği durum sayısı 148’tir.

Bu analiz verileri ışığında ise doğruluk *(accuracy)*, hassasiyet *(precision)*, duyarlılık *(recall)* gibi metrikleri de çıkarabiliriz. 

Bu metrikler Şekil-15’de verilmiştir.

![Şekil-15 Diabetes veri seti Karar Ağacı algoritması metrik sonuçları](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/Ekran_grnts_2023-12-27_001701.png)

Şekil-15 Diabetes veri seti Karar Ağacı algoritması metrik sonuçları

Yukarıda verilen Confusion Matrixle birlikte analiz yapılması gerekirse:

- ***Precision (Hassasiyet):*** Hassasiyet, pozitif olarak tahmin edilen örneklerin gerçekten pozitif olan örneklere oranını göstermektedir. Sınıf 0 için hassasiyet ***0.78***, sınıf 1 için hassasiyet ***0.70*** olarak hesaplandığını gösterir. Bu sonuç bizlere 0 için modelin pozitif olarak tahmin ettiği örneklerin *%78*’inin gerçekten pozitif olduğunu, sınıf 1 için ise *%70*’inin gerçekten pozitif olduğunu gösterir.
- ***Recall (Duyarlılık):*** Duyarlılık, gerçekten pozitif olan örneklerin ne kadarının doğru bir şekilde pozitif olarak tahmin edildiğini gösterir. Sınıf 0 için duyarlılık 0.87, sınıf 1 için duyarlılık 0.55 olarak hesaplandığını gösterir. Bu sonuca göre 0 sınıfı için, gerçek pozitif örneklerin %87’sinin doğru bir şekilde pozitif olarak tahmin edildiğini, 1 sınıfı için gerçek pozitif örneklerin %55’inin doğru bir şekilde pozitif olarak tahmin edildiğini gösterir.
- ***F1-Score:*** F1-Score, hassasiyet ve duyarlılık metriklerinin **harmonik** ortalamasını temsil eder. Sınıf 0 için F1-Score *0.83*, sınıf 1 için F1-Score *0.62* olarak hesaplanmıştır. F1-Score, hem hassasiyeti hem de duyarlılığı dikkate alarak bir sınıflandırma modelinin performansını değerlendirir.
- ***Support:*** Support, her bir sınıfın gerçek veri setinde ne kadar örneğe sahip olduğunu gösterir. Sınıf 0 için 500 örnek, sınıf 1 için 268 örnek bulunmaktadır.
- *Accuracy (Doğruluk):* Accuracy, modelin doğru tahmin ettiği örneklerin toplam örnek sayısına oranını gösterir. Bu Confusion Matrix için değeri 0.76 olarak hesaplanmıştır. Bu da modelin doğru tahmin ettiği örneklerin toplam örneklerin %76’sını oluşturduğundan bahsedebiliriz.
- ***Macro Avg ve Weighted Avg:*** Macro Avg, her sınıfın metrik değerlerinin ağırlıksız ortalamasını temsil ederken, Weigted Avg, her sınıfın metrik değerlerinin örnek sayısına göre ağırlıklı ortalamasını temsil etmektedir.

## RANDOM FOREST KULLANARAK ANALİZ

Karar Ağacının bir türü olan Random Forest algoritmasında veriyi eğitmeden önce belirli şartları Karar Ağacı algoritmasıyla aynıdır. Doğru bir oran elde etmek için temizlenmiş olan diabetes veri setinin belirli bir parametreye bölerek ve karar düğümleri oluşturarak bir sınıflandırma modeli kurgulamak gerekir.

1. **Özellik Seçimi:** İlk olarak, *“Glucose”*, *”BloodPressure”*, *“SkinThickness”*, *“BMI”*, *“DiabetesPedigreeFunction”* ve *“Age”* sütunlarını içeren bir veri çerçevesi oluşturmamız gerekmektedir. Bu sütunlar modelimizin eğitiminde kullanılacak özellikler olarak belirtebiliriz.
2. **Verilerin Bölünmesi:** Denetimli makine öğrenmesi algoritmalarından olan *Random Forest* modelinde verilerin eğitim ve test olarak ikiye ayrılması gerekir. Bundan dolayı verilerimiz, ***train_test_split*** fonksiyonu kullanılarak eğitim ve test setlerine bölünmesi gerekir. Veri setinin oldukça büyük olması ve farklı sonuçlar denenerek **%30**’unun eğitim verisi olarak ayrılmasına karar verdik. Ayrıca rastgele durumu ise karar ağaçlarında olduğu gibi 1 atadık.
3. **Model Oluşturma ve Eğitim:** *Random Forest* Sınıflandırıcısı oluşturuldu. Bu sınıflandırıcı, 15 ağaçtan oluşan bir orman olacak şekilde yapılandırdık. Ayrıca her bir ağacın maksimum derinliği 3 olarak sınırlandırdık. Model eğitim verileri ve test verileri olarak eğittik.
4. **Tahmin Yapma:** Eğitilmiş model *(clf)*, test verileri *(X_Test)* üzerinde tahminlerinde bulunuyor. Son olarak sonuçlar ise *“y_pred”* değişkenine atadık.

Hesaplama sonucu olarak *%79* oranında sınıflandırma başarı oranı elde edilmiştir. Bunu ise bir örnek üzerinden anlatmak gerekirse veri setimiz içerisinde bulunan her bir 100 veri için 79 tanesini doğru bir şekilde sınıflandırdığı sonucu söylenebilmektedir.

## RANDOM FOREST ANALİZ SONUCU

### CONFUSION MATRIX

Şekil-16’da Random Forest modelimizin Confusion Matrix (Karmaşıklık Matrisi) sonuçları verilmiştir.

![Şekil-16 Kurgulanmış olan Random Forest modelinin karmaşıklık matrisi](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/indir_(10).png)

Şekil-16 Kurgulanmış olan Random Forest modelinin karmaşıklık matrisi

İki farklı sınıf (eğitim ve test) verileri göz önüne alındığında Şekil-16 şu şekilde yorumlanabilir.

- ***Doğru Pozitif (True Positive):*** Kurulmuş olan *Random Forest* modelinin doğru bir şekilde pozitif olarak tahmin ettiği durum sayısı *450*’dir.
- ***Yanlış Pozitif (False Positive)***: Kurulmuş olan *Random Forest* modelinin yanlış bir şekilde pozitif olarak tahmin ettiği durum sayısı *50*’dir.
- ***Yanlış Negatif (False Negative):*** Kurulmuş olan *Random Forest* modelinin yanlış bir şekilde negatif olarak tahmin ettiği durum sayısı *113*’tür.
- ***Doğru Negatif (True Negative):*** Kurulmuş olan *Random Forest* modelinin doğru bir şekilde negatif olarak tahmin ettiği durum sayısı *155*’tir.

Bu karmaşıklık matrisi göz önüne alındığında ise doğruluk *(accuracy)*, hassasiyet *(precision)*, duyarlılık *(recall)* gibi metrikleri çıkarabiliriz.

Bu metriklerin sonuçları Şekil-17’de verilmiştir.

![Şekil-17 Random Forest kullanılarak elde edilen metrik sonuçlar](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis/blob/main/dec_rand/DECISION%20TREE%20ve%20RANDOM%20FOREST%20KULLANARAK%20DI%CC%87YABET%206257a084701b4cbc9e5ad678435391a4/Ekran_grnts_2023-12-27_011708.png)

Şekil-17 Random Forest kullanılarak elde edilen metrik sonuçlar

Şekil-16’da verilen karmaşıklık matrisi de göz önüne alındığında Şekil-17’de görülen sonuçlar şu şekilde yorumlanabilir:

- ***Precision (Hassasiyet):*** Hassasiyet, pozitif olarak tahmin edilen örneklerin gerçekten pozitif olan örneklere oranını göstermektedir. Sınıf 0 için hassasiyet *0.80*, sınıf 1 için hassasiyet *0.76* olarak hesaplandığını gösterir. Bu sonuç bizlere 0 sınıfı için modelin pozitif olarak tahmin ettiği örneklerin *%80*’inin gerçekten pozitif olduğunu, sınıf 1 için ise %76’sının gerçekten pozitif olduğunu gösterir.
- ***Recall (Duyarlılık):*** Duyarlılık, gerçekten pozitif olan örneklerin ne kadarının doğru bir şekilde pozitif olarak tahmin edildiğini gösterir. Sınıf 0 için duyarlılık *0.90*, sınıf 1 için duyarlılık *0.58* olarak hesaplandığını gösterir. Bu sonuca göre 0 sınıfı için, gerçek pozitif örneklerin *%90*’ının doğru bir şekilde pozitif olarak tahmin edildiğini, 1 sınıfı için gerçek pozitif örneklerin *%58*’inin doğru bir şekilde pozitif olarak tahmin edildiğini gösterir.
- ***F1-Score:*** F1-Score, hassasiyet ve duyarlılık metriklerinin harmonik ortalamasını temsil eder. Sınıf 0 için F1-Score *0.85*, sınıf 1 için F1-Score *0.66* olarak hesaplanmıştır. F1-Score, hem hassasiyeti hem  de duyarlılığı dikkate alarak bir sınıflandırma modelinin performansını değerlendirir.
- ***Support:*** Support, her bir sınıfın gerçek veri setinde ne kadar örneğe sahip olduğunu gösterir. Sınıf 0 için 500 örnek, sınıf 1 için 268 örnek bulunmaktadır.
- ***Accuracy (Doğruluk):*** Accuracy, modelin doğru tahmin ettiği örneklerin toplam örnek sayısına oranını gösterir. Bu Confusion Matrix için değeri *0.79* olarak hesaplanmıştır. Bu da modelin doğru tahmin ettiği örneklerin toplam örneklerin *%79*’unu oluşturduğundan bahsedebiliriz.
- ***Macro Avg ve Weighted Avg:*** Macro Avg, her sınıfın metrik değerlerinin ağırlıksız ortalamasını temsil ederken, Weigted Avg, her sınıfın metrik değerlerinin örnek sayısına göre ağırlıklı ortalamasını temsil etmektedir.

# SONUÇ

Makine öğrenmesi projesi olarak belirlediğim ***Decision Tree* ve *Random Forest* Kullanarak Diyabet Hastalıkları Veri Analizi ve Sınıflandırılması** çalışması kapsamında *Kaggle* üzerinden elde edilen 769 satır ve 9 sütundan oluşan veri seti üzerinden **Decision Tree** *(Karar Ağacı)* algoritması ve **Random Forest** *(Rastgele Orman)* algoritması kullanarak bir modelleme gerçekleştirilmiştir. Bu modellemeler kurulmadan önce veri seti hakkında birtakım algoritma modelleri geliştirilerek veri setinin daha iyi anlaşılması amaçlanmıştır.

Nitekim bu araştırma, veri seti içerisinde birtakım **outlier** *(aykırı)* verileri tespit edilmiştir. Aykırı veriler araştırma sonucunu doğrudan etkileyebilecek potansiyelde olan veri türleri olduğu için; tespit edilen bu veriler, tekrardan toplanamayacağı veya güncellenemeyeceği için veri seti dağılımı göz önüne alınarak ortalama veya medyan değerlerine göre tekrardan atamalar gerçekleştirilmiştir. 

***Decision Tree*** *(Karar Ağacı)* algoritması kullanılarak *diabetes* veri seti üzerinde yapılan çalışmada sınıflandırma sonucu %77 olarak bulunurken, **Random Forest** *(Rastgele Orman)* algoritması kullanılarak yapılan çalışmada alınan sınıflandırma başarı oranı ise *%79* olarak bulunmuştur. 

Ayrıca bu proje kapsamında bahsedilmeyen ama aynı veri seti üzerinde yapılan ***KNN Algoritması***, ***Lojistik Regresyon Algoritması***, ***SVM*** Algoritması kullanılarak yapılan araştırmamda ise sınıflandırma oranları sırasıyla *%74*, *%77*, *%76* olarak bulunmuştur. Bu çalışmaların raporuna web sayfamdan ulaşabilirsiniz.

Bu beş algoritma sonucu göz önüne alındığında *diabetes* veri seti üzerinde sınıflandırma algoritmaları arasında en başarılı sınıflandırma algoritması **Random Forest *(Rastgele Orman)*** algoritması olarak bulunmuştur.

Bu araştırma görevinde yazılmış olan kodlar **GitHub** profilimden ulaşabilir veya [buraya tıklayarak](https://github.com/ahmetpyrzklnc/diabetes_decisionTree_randomForest_analysis) ulaşabilirsiniz.

Ayrıca bu raporun blog web görüntüsüne [buraya tıklayarak](https://dev-ahmetklnc.notion.site/DECISION-TREE-ve-RANDOM-FOREST-KULLANARAK-D-YABET-HASTALIKLARI-VER-ANAL-Z-ve-SINIFLANDIRILMASI-6257a084701b4cbc9e5ad678435391a4?pvs=4) ulaşabilirsiniz.

Sorularınız ve önerileriniz için [buraya tıklayabilirsiniz.](bit.ly/426SneF)
