-- ===============================================
-- Get Customer by CustomerID
-- ===============================================
IF OBJECT_ID('Customer_GetByID', 'P') IS NOT NULL
    DROP PROCEDURE Customer_GetByID;
GO
CREATE PROCEDURE Customer_GetByID
    @CustomerID INT
AS
BEGIN
    SELECT *
    FROM Customers
    WHERE CustomerID = @CustomerID AND IsActive = 1;
END;

-- ===============================================
-- Update Customer Loyalty Points
-- ===============================================
IF OBJECT_ID('Customer_UpdateLoyaltyPoints', 'P') IS NOT NULL
    DROP PROCEDURE Customer_UpdateLoyaltyPoints;
GO
CREATE PROCEDURE Customer_UpdateLoyaltyPoints
    @CustomerID INT,
    @LoyaltyPoints INT
AS
BEGIN
    UPDATE Customers
    SET LoyaltyPoints = @LoyaltyPoints,
        UpdatedAt = GETDATE()
    WHERE CustomerID = @CustomerID AND IsActive = 1;
END;