# Agent Instructions

## Mục tiêu

Làm việc chính xác, tối giản và có thể kiểm chứng. Ưu tiên hoàn thành đúng yêu cầu người dùng, giữ thay đổi trong phạm vi cần thiết và không phá vỡ hành vi hiện có.

## Quy trình làm việc

1. Đọc yêu cầu đầy đủ và xác định file, module hoặc hành vi liên quan.
2. Kiểm tra cấu trúc dự án, quy ước hiện có và trạng thái thay đổi trước khi sửa.
3. Nêu giả thuyết ngắn gọn về nguyên nhân hoặc cách triển khai.
4. Thực hiện thay đổi nhỏ nhất có thể.
5. Chạy kiểm tra phù hợp nhất ngay sau khi chỉnh sửa: test, build, lint hoặc typecheck.
6. Nếu kiểm tra thất bại, sửa trong cùng phạm vi và chạy lại kiểm tra đó.
7. Tóm tắt file đã thay đổi, kết quả kiểm tra và các vấn đề còn lại.

## Quy tắc chỉnh sửa

- Giữ phong cách, kiến trúc và API hiện có của dự án.
- Không hoàn tác thay đổi của người dùng.
- Không sửa các lỗi không liên quan đến yêu cầu.
- Tránh thêm abstraction hoặc dependency nếu chưa cần thiết.
- Không tạo commit hoặc branch nếu chưa được yêu cầu.
- Chỉ thêm comment khi logic không thể tự giải thích rõ ràng.
- Ưu tiên nội dung ASCII trừ khi dự án đã dùng Unicode cho mục đích cụ thể.

## Kiểm thử và xác minh

- Ưu tiên kiểm tra hẹp nhất có thể cho phần vừa thay đổi.
- Khi không có test, thực hiện build, lint, typecheck hoặc kiểm tra thủ công phù hợp.
- Không báo hoàn thành nếu chưa xác minh, trừ khi môi trường không cho phép chạy kiểm tra; khi đó phải nêu rõ lý do.

## Giao tiếp

- Trả lời ngắn gọn, rõ ràng và bằng ngôn ngữ của người dùng khi phù hợp
- Khi báo lỗi, nêu nguyên nhân, vị trí liên quan và hướng xử lý.
- Khi hoàn thành, nêu thay đổi chính và lệnh kiểm tra đã chạy.
