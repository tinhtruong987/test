use fashion_shop
go

-- Lấy tất cả khách hàng đang hoạt động
CREATE PROCEDURE Customer_GetAll
AS
BEGIN
    SELECT * FROM Customers WHERE IsActive = 1
END
GO

-- Lấy 1 khách hàng theo ID
CREATE PROCEDURE Customer_GetByID @CustomerID INT
AS
BEGIN
    SELECT * FROM Customers WHERE CustomerID = @CustomerID
END
GO

-- Tạo khách hàng mới
CREATE PROCEDURE Customer_Create
    @Name NVARCHAR(100),
    @Phone NVARCHAR(20),
    @Email NVARCHAR(100),
    @Address NVARCHAR(255),
    @LoyaltyPoints INT
AS
BEGIN
    INSERT INTO Customers (Name, Phone, Email, Address, LoyaltyPoints, IsActive, CreatedAt)
    VALUES (@Name, @Phone, @Email, @Address, @LoyaltyPoints, 1, GETDATE())
END
GO

-- Cập nhật khách hàng
CREATE PROCEDURE Customer_Update
    @CustomerID INT,
    @Name NVARCHAR(100) = NULL,
    @Phone NVARCHAR(20) = NULL,
    @Email NVARCHAR(100) = NULL,
    @Address NVARCHAR(255) = NULL,
    @LoyaltyPoints INT = NULL
AS
BEGIN
    UPDATE Customers
    SET
        Name = ISNULL(@Name, Name),
        Phone = ISNULL(@Phone, Phone),
        Email = ISNULL(@Email, Email),
        Address = ISNULL(@Address, Address),
        LoyaltyPoints = ISNULL(@LoyaltyPoints, LoyaltyPoints),
        UpdatedAt = GETDATE()
    WHERE CustomerID = @CustomerID
END
GO

-- Xóa mềm (soft delete)
CREATE PROCEDURE Customer_Delete
    @CustomerID INT
AS
BEGIN
    UPDATE Customers SET IsActive = 0, UpdatedAt = GETDATE() WHERE CustomerID = @CustomerID
END
GO

CREATE PROCEDURE Customer_Activate
    @CustomerID INT
AS
BEGIN
    UPDATE Customers
    SET IsActive = 1,
        UpdatedAt = GETDATE()
    WHERE CustomerID = @CustomerID
END
GO