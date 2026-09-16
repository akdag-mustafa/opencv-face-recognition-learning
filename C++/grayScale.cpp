#include <iostream>
#include <opencv2/opencv.hpp>

// Renkli görüntüyü kendi algoritmamızla griye çevirir.
cv::Mat kendiGrayAlgoritmamiz(const cv::Mat &renkliGoruntu)
{
    /*
        Renkli görüntü:
        CV_8UC3 → 8 bit, unsigned, 3 kanal (BGR)

        Oluşturacağımız gri görüntü:
        CV_8UC1 → 8 bit, unsigned, 1 kanal
    */

    cv::Mat griGoruntu(
        renkliGoruntu.rows,
        renkliGoruntu.cols,
        CV_8UC1);

    // Görüntünün bütün satırlarını dolaşıyoruz.
    for (int y = 0; y < renkliGoruntu.rows; y++)
    {
        // Satırdaki bütün sütunları dolaşıyoruz.
        for (int x = 0; x < renkliGoruntu.cols; x++)
        {
            /*
                OpenCV renk kanallarını BGR sırasıyla tutar:

                piksel[0] → Blue
                piksel[1] → Green
                piksel[2] → Red
            */

            cv::Vec3b piksel =
                renkliGoruntu.at<cv::Vec3b>(y, x);

            unsigned char b = piksel[0];
            unsigned char g = piksel[1];
            unsigned char r = piksel[2];

            /*
                İnsan gözü yeşile daha duyarlı,
                maviye ise daha az duyarlıdır.

                Gray = 0.114B + 0.587G + 0.299R
            */

            unsigned char griDeger =
                static_cast<unsigned char>(
                    0.114 * b +
                    0.587 * g +
                    0.299 * r);

            // Hesaplanan değeri gri görüntüye yazıyoruz.
            griGoruntu.at<unsigned char>(y, x) = griDeger;
        }
    }

    return griGoruntu;
}

int main()
{
    // 0, Mac'in varsayılan kamerasını temsil eder.
    cv::VideoCapture kamera(0);

    // Kamera açılamadıysa programı sonlandır.
    if (!kamera.isOpened())
    {
        std::cerr << "Kamera acilamadi." << std::endl;
        return 1;
    }

    cv::Mat renkliGoruntu;

    while (true)
    {
        // Kameradan bir kare al.
        kamera >> renkliGoruntu;

        // Boş görüntü geldiyse döngüyü bitir.
        if (renkliGoruntu.empty())
        {
            std::cerr << "Goruntu alinamadi." << std::endl;
            break;
        }

        // cvtColor kullanmadan kendi fonksiyonumuzu çağırıyoruz.
        cv::Mat griGoruntu =
            kendiGrayAlgoritmamiz(renkliGoruntu);

        // Renkli ve gri görüntüleri göster.
        cv::imshow("Original", renkliGoruntu);

        cv::imshow(
            "Kendi C++ Gray Algoritmamiz",
            griGoruntu);

        // Klavyeden q tuşuna basılırsa çık.
        if (cv::waitKey(1) == 'q')
        {
            break;
        }
    }

    // Kamera ve pencereleri serbest bırak.
    kamera.release();
    cv::destroyAllWindows();

    return 0;
}