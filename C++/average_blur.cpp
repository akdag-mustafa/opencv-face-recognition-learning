#include <iostream>
#include <algorithm>
#include <opencv2/opencv.hpp>

cv::Mat kendiBlurAlgoritmamiz(const cv::Mat &goruntu, int kernelBoyutu)
{
    if (kernelBoyutu % 2 == 0)
    {
        throw std::invalid_argument(
            "Kernel boyutu tek sayi olmalidir.");
    }

    cv::Mat bulanmisGoruntu(
        goruntu.rows,
        goruntu.cols,
        CV_8UC3);

    int kenarBosluk = kernelBoyutu / 2;
    int pikselSayisi = kernelBoyutu * kernelBoyutu;

    for (int y = 0; y < goruntu.rows; y++)
    {
        for (int x = 0; x < goruntu.cols; x++)
        {
            int toplamB = 0;
            int toplamG = 0;
            int toplamR = 0;

            for (int ky = -kenarBosluk;
                 ky <= kenarBosluk;
                 ky++)
            {
                for (int kx = -kenarBosluk;
                     kx <= kenarBosluk;
                     kx++)
                {
                    int komsuY = std::clamp(
                        y + ky,
                        0,
                        goruntu.rows - 1);

                    int komsuX = std::clamp(
                        x + kx,
                        0,
                        goruntu.cols - 1);

                    cv::Vec3b piksel =
                        goruntu.at<cv::Vec3b>(
                            komsuY,
                            komsuX);

                    toplamB += piksel[0];
                    toplamG += piksel[1];
                    toplamR += piksel[2];
                }
            }

            cv::Vec3b &sonucPiksel =
                bulanmisGoruntu.at<cv::Vec3b>(y, x);

            sonucPiksel[0] = static_cast<unsigned char>(
                toplamB / pikselSayisi);

            sonucPiksel[1] = static_cast<unsigned char>(
                toplamG / pikselSayisi);

            sonucPiksel[2] = static_cast<unsigned char>(
                toplamR / pikselSayisi);
        }
    }

    return bulanmisGoruntu;
}

int main()
{
    cv::VideoCapture kamera(0);

    kamera.set(cv::CAP_PROP_FRAME_WIDTH, 320);
    kamera.set(cv::CAP_PROP_FRAME_HEIGHT, 240);

    if (!kamera.isOpened())
    {
        std::cerr << "Kamera acilamadi." << std::endl;
        return 1;
    }

    cv::Mat goruntu;

    while (true)
    {
        kamera >> goruntu;

        if (goruntu.empty())
        {
            std::cerr << "Goruntu alinamadi." << std::endl;
            break;
        }

        cv::Mat blurredGoruntu =
            kendiBlurAlgoritmamiz(goruntu, 5);

        cv::imshow("Original", goruntu);
        cv::imshow("Manual C++ Blur", blurredGoruntu);

        if (cv::waitKey(1) == 'q')
        {
            break;
        }
    }

    kamera.release();
    cv::destroyAllWindows();
    return 0;
}